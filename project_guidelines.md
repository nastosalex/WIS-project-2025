# PetPal E-shop Project Guidelines

## Current Project Status

### Completed Parts

#### Part A: Frontend Development
- Created responsive homepage with modern design
- Implemented product showcase with slideshow
- Added features section highlighting key benefits
- Created about us section with company information
- Implemented responsive navigation
- Added footer with team information
- Styled with CSS using modern practices
- All text content in Greek

#### Part B: Backend Development
- Set up Flask server with MongoDB integration
- Implemented REST API endpoints:
  - `/search` - Search products by name
  - `/like` - Increment product likes
  - `/popular-products` - Get top 5 most liked products
- Added text search functionality with MongoDB indexing
- Implemented error handling
- Connected to MongoDB Atlas
- Populated database with sample products

### Project Structure
```
project/
├── backend/
│   ├── app.py              # Flask server and API endpoints
│   ├── requirements.txt    # Python dependencies
│   └── .env               # Environment variables (MongoDB URI)
├── public/
│   ├── homepage.html      # Main landing page
│   ├── products.html      # Products listing page
│   ├── style.css          # Main stylesheet
│   ├── products.js        # Dynamic logic file (to be created)
│   └── assets/
│       └── images/        # Product and logo images
└── docker/                # Docker configuration files
```

## Next Steps

### Part C: Dynamic Frontend (JavaScript)
1. Create `products.js` in the `/public/` directory
2. Implement vanilla JavaScript functionality:
   - Search Input:
     - Send GET requests to `/search?name=<query>` on form submit or keyup
     - Clear and dynamically render product results
   - Like Click:
     - Send POST requests to `/like` with product ID
     - Update displayed like count
   - Homepage Slideshow:
     - Load popular products on homepage load
     - Populate slideshow with product images and names
3. Requirements:
   - Use only vanilla JavaScript
   - Use `fetch()` for all requests
   - Set `Content-Type: application/json` for POST requests
   - No external libraries or frameworks

### Part D: Docker (Optional)
1. Create Docker configuration in `/docker/` directory:
   - Dockerfile for static server (serving `/public/`)
   - Dockerfile for Flask API
   - Use official MongoDB image
2. Create `docker-compose.yml` to orchestrate:
   - Static file server
   - Flask API service
   - MongoDB service

## Technical Guidelines

### Backend (Flask)
- Keep using the existing app.py structure
- Maintain current API endpoints
- Follow RESTful principles
- Keep error handling consistent
- Use environment variables for configuration

### Frontend
- Maintain current responsive design
- Keep Greek language implementation
- Follow existing CSS structure
- Maintain current file organization
- Use vanilla JavaScript only
- No external libraries or frameworks

### JavaScript Implementation
- Use `fetch()` for all API calls
- Set proper headers for POST requests
- Handle API responses appropriately
- Implement error handling
- Keep code modular and maintainable

## Important Notes
1. All text content should remain in Greek
2. Maintain current project structure
3. Keep code style consistent
4. No external libraries or frameworks allowed
5. Use only vanilla JavaScript for dynamic features

## Getting Started
1. Clone the repository
2. Set up environment variables
3. Install dependencies
4. Run the Flask server
5. Access the application at localhost:5000

## Dependencies
- Python 3.x
- Flask 3.0.2
- Flask-PyMongo 2.3.0
- Flask-CORS 4.0.0
- python-dotenv 1.0.1
- Docker (optional)
- Docker Compose (optional)

## Contact
For any questions or clarifications, contact the team members:
- Anastasios
- Konstantinos
- Ilias 