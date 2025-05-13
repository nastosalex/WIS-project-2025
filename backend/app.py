from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
from bson import ObjectId
import os
from dotenv import load_dotenv

# Φόρτωση μεταβλητών περιβάλλοντος
from pathlib import Path
load_dotenv(dotenv_path=Path(__file__).parent / ".env")

app = Flask(__name__)
CORS(app)

# Ρύθμιση MongoDB
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
mongo = PyMongo(app)

# Create text index on name field
mongo.db.products.create_index([("name", "text")])

@app.route('/search', methods=['GET'])
def search_products():
    query = request.args.get('name', '')
    
    if query:
        # Αναζήτηση κειμένου στο πεδίο ονόματος
        products = list(mongo.db.products.find(
            {"$text": {"$search": query}},
            {"score": {"$meta": "textScore"}}
        ).sort([("score", {"$meta": "textScore"}), ("price", -1)]))
    else:
        # Επιστροφή όλων των προϊόντων ταξινομημένα κατά τιμή
        products = list(mongo.db.products.find().sort("price", -1))
    
    # Μετατροπή του ObjectId σε string για JSON σειριοποίηση
    for product in products:
        product['_id'] = str(product['_id'])
        if 'score' in product:
            del product['score']
    
    return jsonify(products)

@app.route('/like', methods=['POST'])
def like_product():
    data = request.get_json()
    product_id = data.get('id')
    
    if not product_id:
        return jsonify({"error": "Product ID is required"}), 400
    
    try:
        result = mongo.db.products.update_one(
            {"_id": ObjectId(product_id)},
            {"$inc": {"likes": 1}}
        )
        
        if result.modified_count == 0:
            return jsonify({"error": "Product not found"}), 404
            
        updated_product = mongo.db.products.find_one({"_id": ObjectId(product_id)})
        updated_product['_id'] = str(updated_product['_id'])
        return jsonify(updated_product)
        
    except Exception as e:
        return jsonify({"error": "An error occurred"}), 400

@app.route('/popular-products', methods=['GET'])
def get_popular_products():
    products = list(mongo.db.products.find().sort("likes", -1).limit(5))
    
    # Μετατροπή του ObjectId σε string για JSON σειριοποίηση
    for product in products:
        product['_id'] = str(product['_id'])
    
    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=False) 