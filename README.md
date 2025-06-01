# PetPal E-shop

A modern e-commerce platform for pet products, built with Flask, MongoDB, and vanilla JavaScript.

## 🌟 Features

- **Responsive Design**: Modern, mobile-friendly interface
- **Dynamic Product Search**: Real-time search functionality
- **Product Showcase**: Interactive slideshow of popular products
- **Like System**: Users can like their favorite products
- **Greek Language Support**: Full Greek language implementation
- **Docker Support**: Easy deployment with Docker containers

## 🛠️ Tech Stack

- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Backend**: Python Flask
- **Database**: MongoDB Atlas
- **Server**: Nginx
- **Containerization**: Docker & Docker Compose

## 📋 Prerequisites

- Python 3.x
- Docker and Docker Compose (for containerized deployment)
- MongoDB Atlas account (for database)

## 🚀 Getting Started

### Local Development

1. Clone the repository:
   ```bash
   git clone https://github.com/nastosalex/WIS-project-2025.git
   cd WIS-project-2025
   ```

2. Set up the backend:
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the backend directory:
   ```
   MONGODB_URI=your_mongodb_connection_string
   ```

4. Run the Flask server:
   ```bash
   python app.py
   ```

5. Serve the frontend:
   ```bash
   cd public
   python -m http.server 8000
   ```

6. Access the application at `http://localhost:8000`

### Docker Deployment

1. Build and start the containers:
   ```bash
   docker-compose -f docker/docker-compose.yml up --build
   ```

2. Access the application at `http://localhost`

## 📁 Project Structure

```
project/
├── backend/
│   ├── app.py              # Flask server and API endpoints
│   └── requirements.txt    # Python dependencies
├── public/
│   ├── homepage.html      # Main landing page
│   ├── products.html      # Products listing page
│   ├── style.css          # Main stylesheet
│   ├── products.js        # Dynamic logic
│   └── assets/
│       └── images/        # Product and logo images
└── docker/                # Docker configuration files
```

## 🔌 API Endpoints

- `GET /search?name=<query>` - Search products by name
- `POST /like` - Increment product likes
- `GET /popular-products` - Get top 5 most liked products

## 👥 Team Members

- Anastasios
- Konstantinos

## 📝 License

This project is part of the Web Information Systems course at the Aristotle University

## 🔒 Security

The project follows security best practices:
- Environment variables for sensitive data
- CORS configuration
- Input validation
- Error handling

## 🤝 Contributing

This is a course project and is not open for contributions.

## 📞 Contact

For any questions or clarifications, please contact the team members.
