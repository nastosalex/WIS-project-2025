// API endpoint for popular products
const API_BASE_URL = 'http://localhost:5000';  // Adjust this based on your backend URL
const POPULAR_PRODUCTS_ENDPOINT = `${API_BASE_URL}/popular-products`;

// DOM Elements
const slideshow = document.querySelector('.slideshow');
const dotsContainer = document.querySelector('.slideshow-dots');

// Load and display popular products
async function loadPopularProducts() {
    try {
        const response = await fetch(POPULAR_PRODUCTS_ENDPOINT);
        if (!response.ok) throw new Error('Failed to load popular products');
        
        const products = await response.json();
        updateSlideshow(products);
    } catch (error) {
        console.error('Load popular products error:', error);
        showError('Αποτυχία φόρτωσης δημοφιλών προϊόντων.');
    }
}

function updateSlideshow(products) {
    // Clear existing slides
    slideshow.innerHTML = '';
    dotsContainer.innerHTML = '';

    // Create new slides and dots
    products.forEach((product, index) => {
        // Handle image path
        const imagePath = product.photo 
            ? (product.photo.startsWith('assets/') ? product.photo : `assets/images/${product.photo}`)
            : 'assets/images/image.png';

        // Create slide
        const slide = document.createElement('div');
        slide.className = `slide ${index === 0 ? 'active' : ''}`;
        slide.innerHTML = `
            <img src="${imagePath}" class="slide-image" alt="${product.name}">
            <div class="slide-caption">${product.name} - ${product.description}</div>
        `;
        slideshow.appendChild(slide);

        // Create dot
        const dot = document.createElement('span');
        dot.className = `dot ${index === 0 ? 'active' : ''}`;
        dot.addEventListener('click', () => showSlide(index));
        dotsContainer.appendChild(dot);
    });

    // Reset slideshow state
    currentSlide = 0;
}

// Slideshow functionality
let currentSlide = 0;
const prevButton = document.querySelector('.prev');
const nextButton = document.querySelector('.next');

function showSlide(n) {
    const slides = document.querySelectorAll('.slide');
    const dots = document.querySelectorAll('.dot');
    
    slides.forEach(slide => slide.classList.remove('active'));
    dots.forEach(dot => dot.classList.remove('active'));
    
    currentSlide = (n + slides.length) % slides.length;
    
    slides[currentSlide].classList.add('active');
    dots[currentSlide].classList.add('active');
}

function nextSlide() {
    showSlide(currentSlide + 1);
}

function prevSlide() {
    showSlide(currentSlide - 1);
}

// Event Listeners
prevButton.addEventListener('click', prevSlide);
nextButton.addEventListener('click', nextSlide);

// Auto-advance slideshow
let slideshowInterval = setInterval(nextSlide, 5000);

// Pause slideshow on hover
slideshow.addEventListener('mouseenter', () => {
    clearInterval(slideshowInterval);
});

slideshow.addEventListener('mouseleave', () => {
    slideshowInterval = setInterval(nextSlide, 5000);
});

function showError(message) {
    // You can implement a more sophisticated error display
    console.error(message);
}

// Initialize the slideshow
document.addEventListener('DOMContentLoaded', loadPopularProducts); 