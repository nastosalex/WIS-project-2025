# WIS Project 2025 — Pet Toy eShop

A playful, modern eCommerce web app for a fictional pet toy store, built by a team of 3. This document outlines the full requirements and scope of the project, divided into three distinct development roles and steps.

---

## 👥 Team Roles

- **A. Static Website Developer (HTML/CSS)**
- **B. Backend Developer (Flask REST API + MongoDB)**
- **C. Dynamic Frontend Developer (JavaScript + API Integration)**

---

## ✅ Project Tasks & Requirements

### 🔷 Part A: Static Website (HTML5 + CSS3)

Develop two HTML pages:

#### 1. `homepage.html`
- Header with logo and navigation buttons
- Title with the name of the eShop
- Slideshow with product images
- Main body can contain additional promotional elements
- Footer with team member names

#### 2. `products.html`
- Header (same as above)
- Search bar at the top
- Dynamic product grid (initially hard-coded or empty)
- Each product must display:
  - Product Image
  - Product Name
  - Short Description
- Footer with team names

**Tools:** HTML5, CSS3

---

### 🔷 Part B: Flask REST API + MongoDB

Build a Python API with `Flask`, `Flask-PyMongo`, `Flask-CORS`, and `numpy`. Store at least 20 products in MongoDB with the following fields:

- `name`: string  
- `photo`: URL or base64  
- `description`: string  
- `likes`: integer  
- (Optional: `price`, `category`, etc.)

#### API Endpoints:

##### `GET /search?name=`
- Search products by partial/full name (text index required on `name`)
- If query is empty (`""`), return all products
- Sort results by price descending if multiple matches

##### `POST /like`
- Increment the likes of a product
- Expects JSON: `{ "id": "PRODUCT_ID" }`

##### `GET /popular-products`
- Return top 5 most liked products

#### Technical Notes:
- Run Flask on `http://127.0.0.1:5000`
- Use only approved libraries (Flask, Flask-PyMongo, Flask-CORS, numpy)

---

### 🔷 Part C: Dynamic Interaction with JavaScript

Write a JS file `products.js` to power the following:

#### Interaction 1: Product Search
- On search input, send `GET /search` request
- Clear previous results and render new ones in the product grid

#### Interaction 2: Like Product
- On click of product image, send `POST /like` request
- Optionally update like count in UI

#### Interaction 3: Slideshow with Popular Products
- On homepage, dynamically load slideshow with data from `GET /popular-products`
- Display name + photo for each

**Tools:** Vanilla JS or lightweight frameworks (e.g., Alpine.js)

