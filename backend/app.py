from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
from bson import ObjectId
import os
from dotenv import load_dotenv
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Φόρτωση μεταβλητών περιβάλλοντος
from pathlib import Path
load_dotenv(dotenv_path=Path(__file__).parent / ".env")

app = Flask(__name__)
CORS(app)

# Ρύθμιση MongoDB
mongo_uri = os.getenv("MONGO_URI")
if not mongo_uri:
    logger.error("MONGO_URI environment variable is not set")
    raise ValueError("MONGO_URI environment variable is not set")

logger.info("Attempting to connect to MongoDB...")
app.config["MONGO_URI"] = mongo_uri

try:
    mongo = PyMongo(app)
    # Test the connection
    mongo.db.command('ping')
    logger.info("Successfully connected to MongoDB!")
    
    # List all collections to verify database access
    collections = mongo.db.list_collection_names()
    logger.info(f"Available collections: {collections}")
    
except Exception as e:
    logger.error(f"Error connecting to MongoDB: {str(e)}")
    raise ValueError(f"Error connecting to MongoDB: {str(e)}")

# Create text index on name field
try:
    mongo.db.products.create_index([("name", "text")])
    logger.info("Successfully created text index on 'name' field")
except Exception as e:
    logger.error(f"Error creating index: {str(e)}")
    raise ValueError(f"Error creating index: {str(e)}")

@app.route('/search', methods=['GET'])
def search_products():
    query = request.args.get('name', '').strip()
    
    if not query:
        # Return all products sorted by price if no query
        products = list(mongo.db.products.find().sort("price", -1))
    else:
        # First try exact match
        exact_match = list(mongo.db.products.find(
            {"name": {"$regex": f"^{query}$", "$options": "i"}}
        ))
        
        if exact_match:
            # If we found an exact match, return only that
            products = exact_match
        else:
            # If no exact match, search for partial matches
            products = list(mongo.db.products.find(
                {"$text": {"$search": query}},
                {"score": {"$meta": "textScore"}}
            ).sort([("score", {"$meta": "textScore"}), ("price", -1)]))
    
    # Convert ObjectId to string for JSON serialization
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

@app.route('/test-db', methods=['GET'])
def test_db():
    try:
        # Test connection
        mongo.db.command('ping')
        
        # Get all collections
        collections = mongo.db.list_collection_names()
        
        # Get sample data from each collection
        data = {}
        for collection in collections:
            sample = list(mongo.db[collection].find().limit(1))
            if sample:
                # Convert ObjectId to string for JSON serialization
                sample[0]['_id'] = str(sample[0]['_id'])
            data[collection] = sample
        
        return jsonify({
            "status": "success",
            "message": "Successfully connected to MongoDB",
            "collections": collections,
            "sample_data": data
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route('/test-products', methods=['GET'])
def test_products():
    try:
        products = list(mongo.db.products.find())
        for product in products:
            product['_id'] = str(product['_id'])
        return jsonify({"products": products})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False) 