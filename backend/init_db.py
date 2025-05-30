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
    },
    {
        "name": "Rope Toy",
        "description": "Δυνατό σχοινί για σκύλους με κόμπους",
        "image": "assets/images/image copy 2.png",
        "price": 8.99,
        "likes": 0
    },
    {
        "name": "Cat Tree",
        "description": "Ψηλό δέντρο για γάτες με κουκκίδες",
        "image": "assets/images/image.png",
        "price": 89.99,
        "likes": 0
    },
    {
        "name": "Squeaky Duck",
        "description": "Παπαρούνα με τρίξιμο για σκύλους",
        "image": "assets/images/image copy.png",
        "price": 7.99,
        "likes": 0
    },
    {
        "name": "Laser Pointer",
        "description": "Δείκτης λέιζερ για διασκέδαση γάτας",
        "image": "assets/images/image copy 2.png",
        "price": 5.99,
        "likes": 0
    },
    {
        "name": "Frisbee",
        "description": "Δίσκος για σκύλους με ανθεκτικό υλικό",
        "image": "assets/images/image.png",
        "price": 12.99,
        "likes": 0
    },
    {
        "name": "Cat Tunnel",
        "description": "Σήραγγα για γάτες με τρύπες",
        "image": "assets/images/image copy.png",
        "price": 24.99,
        "likes": 0
    },
    {
        "name": "Kong Classic",
        "description": "Κλασικό παιχνίδι για σκύλους με λιχουδιές",
        "image": "assets/images/image copy 2.png",
        "price": 18.99,
        "likes": 0
    },
    {
        "name": "Mouse Teaser",
        "description": "Ποντίκι με κορδέλα για γάτες",
        "image": "assets/images/image.png",
        "price": 6.99,
        "likes": 0
    },
    {
        "name": "Ball Launcher",
        "description": "Συσκευή εκτόξευσης μπάλας για σκύλους",
        "image": "assets/images/image copy.png",
        "price": 29.99,
        "likes": 0
    },
    {
        "name": "Cat Bed",
        "description": "Απαλό κρεβάτι για γάτες",
        "image": "assets/images/image copy 2.png",
        "price": 39.99,
        "likes": 0
    },
    {
        "name": "Tug Rope",
        "description": "Σχοινί τράβηγμα για σκύλους",
        "image": "assets/images/image.png",
        "price": 11.99,
        "likes": 0
    },
    {
        "name": "Catnip Toys Set",
        "description": "Σετ παιχνιδιών με catnip για γάτες",
        "image": "assets/images/image copy.png",
        "price": 15.99,
        "likes": 0
    },
    {
        "name": "Floating Ball",
        "description": "Μπάλα που επιπλέει στο νερό για σκύλους",
        "image": "assets/images/image copy 2.png",
        "price": 9.99,
        "likes": 0
    },
    {
        "name": "Window Perch",
        "description": "Περίπτερο για γάτες στο παράθυρο",
        "image": "assets/images/image.png",
        "price": 34.99,
        "likes": 0
    },
    {
        "name": "Treat Puzzle",
        "description": "Παζλ με λιχουδιές για σκύλους",
        "image": "assets/images/image copy.png",
        "price": 22.99,
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