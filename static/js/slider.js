let currentSlide = 0;

function showSlide(index) {
    const slides = document.querySelector(".slides");
    const totalSlides = slides.children.length;

    if (index < 0) {
        currentSlide = totalSlides - 1;
    } else if (index >= totalSlides) {
        currentSlide = 0;
    } else {
        currentSlide = index;
    }

    slides.style.transform = `translateX(-${currentSlide * 100}%)`;
}

function moveSlide(direction) {
    showSlide(currentSlide + direction);
}

// Auto-Slide (Optional)
setInterval(() => moveSlide(1), 5000); // Slide every 5 seconds

