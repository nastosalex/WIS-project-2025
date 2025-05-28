// API endpoints
const API_BASE_URL = 'http://localhost:5000';  // Adjust this based on your backend URL
const SEARCH_ENDPOINT = `${API_BASE_URL}/search`;
const LIKE_ENDPOINT = `${API_BASE_URL}/like`;
const POPULAR_PRODUCTS_ENDPOINT = `${API_BASE_URL}/popular-products`;

// DOM Elements
const searchInput = document.querySelector('.search-bar input');
const productGrid = document.querySelector('.product-grid');

// Like tracking
function getLikedProducts() {
    const likedProducts = localStorage.getItem('likedProducts');
    return likedProducts ? JSON.parse(likedProducts) : [];
}

function hasLikedProduct(productId) {
    const likedProducts = getLikedProducts();
    return likedProducts.includes(productId);
}

function addLikedProduct(productId) {
    const likedProducts = getLikedProducts();
    if (!likedProducts.includes(productId)) {
        likedProducts.push(productId);
        localStorage.setItem('likedProducts', JSON.stringify(likedProducts));
    }
}

// Interaction 1: Search functionality
searchInput.addEventListener('input', debounce(async (e) => {
    const searchQuery = e.target.value.trim();
    if (searchQuery.length === 0) {
        // If search is empty, show all products
        await loadAllProducts();
        return;
    }

    try {
        const response = await fetch(`${SEARCH_ENDPOINT}?name=${encodeURIComponent(searchQuery)}`);
        if (!response.ok) throw new Error('Search failed');
        
        const products = await response.json();
        displayProducts(products);
    } catch (error) {
        console.error('Search error:', error);
        showError('Αποτυχία αναζήτησης. Παρακαλώ δοκιμάστε ξανά.');
    }
}, 300));

// Interaction 2: Like functionality
productGrid.addEventListener('click', async (e) => {
    const productCard = e.target.closest('.product-card');
    if (!productCard) return;

    const productId = productCard.dataset.productId;
    if (!productId) return;

    // Check if user has already liked this product
    if (hasLikedProduct(productId)) {
        showError('Έχετε ήδη κάνει like σε αυτό το προϊόν.');
        return;
    }

    try {
        const response = await fetch(LIKE_ENDPOINT, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ id: productId })
        });

        if (!response.ok) throw new Error('Like failed');
        
        const updatedProduct = await response.json();
        updateProductLikes(productCard, updatedProduct.likes);
        addLikedProduct(productId); // Add to liked products
    } catch (error) {
        console.error('Like error:', error);
        showError('Αποτυχία ενημέρωσης likes. Παρακαλώ δοκιμάστε ξανά.');
    }
});

// Helper Functions
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

function displayProducts(products) {
    // Clear existing products
    productGrid.innerHTML = '';
    
    if (products.length === 0) {
        productGrid.innerHTML = '<p class="no-results">Δεν βρέθηκαν προϊόντα</p>';
        return;
    }

    products.forEach(product => {
        const productCard = createProductCard(product);
        productGrid.appendChild(productCard);
    });
}

function createProductCard(product) {
    const card = document.createElement('div');
    card.className = 'product-card';
    card.dataset.productId = product._id;

    const hasLiked = hasLikedProduct(product._id);
    const likeButtonClass = hasLiked ? 'liked' : '';

    card.innerHTML = `
        <img src="${product.image || 'assets/images/image.png'}" alt="${product.name}">
        <h3>${product.name}</h3>
        <p>${product.description}</p>
        <div class="product-likes ${likeButtonClass}">
            <span class="likes-count">${product.likes || 0}</span> likes
        </div>
    `;

    return card;
}

function updateProductLikes(productCard, newLikes) {
    const likesCount = productCard.querySelector('.likes-count');
    if (likesCount) {
        likesCount.textContent = newLikes;
    }
    productCard.querySelector('.product-likes').classList.add('liked');
}

function showError(message) {
    // You can implement a more sophisticated error display
    alert(message);
}

// Load all products on page load
async function loadAllProducts() {
    try {
        const response = await fetch(`${SEARCH_ENDPOINT}`);
        if (!response.ok) throw new Error('Failed to load products');
        
        const products = await response.json();
        displayProducts(products);
    } catch (error) {
        console.error('Load products error:', error);
        showError('Αποτυχία φόρτωσης προϊόντων. Παρακαλώ ανανεώστε τη σελίδα.');
    }
}

// Initialize the page
document.addEventListener('DOMContentLoaded', loadAllProducts); 