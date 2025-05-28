from app import mongo
from bson import ObjectId

# Sample products data
sample_products = [
    {
        "name": "Interactive Ball",
        "description": "Έξυπνη μπάλα για σκύλους με ήχο και φωτισμό",
        "image": "assets/images/image.png",
        "price": 19.99,
        "likes": 0
    },
    {
        "name": "Plush Mouse",
        "description": "Απαλό ποντίκι για γάτες με catnip",
        "image": "assets/images/image copy.png",
        "price": 14.99,
        "likes": 0
    },
    {
        "name": "Chew Bone",
        "description": "Δυνατό κόκαλο για σκύλους με βιταμίνες",
        "image": "assets/images/image copy 2.png",
        "price": 9.99,
        "likes": 0
    },
    {
        "name": "Feather Wand",
        "description": "Ράβδος με φτερά για διασκέδαση γάτας",
        "image": "assets/images/image.png",
        "price": 12.99,
        "likes": 0
    },
    {
        "name": "Treat Ball",
        "description": "Μπάλα με λιχουδιές για ενεργό παιχνίδι",
        "image": "assets/images/image copy.png",
        "price": 15.99,
        "likes": 0
    }
]

def init_db():
    # Clear existing products
    mongo.db.products.delete_many({})
    
    # Insert sample products
    result = mongo.db.products.insert_many(sample_products)
    print(f"Inserted {len(result.inserted_ids)} products")

if __name__ == "__main__":
    init_db() 