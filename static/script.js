document.addEventListener('DOMContentLoaded', function() {
    const mobileMenu = document.querySelector('.menu-toggle');
    const navMenu = document.querySelector('.nav-menu');
    const mobileSearchIcon = document.querySelector('.mobile-search-icon');
    const mobileSearchForm = document.querySelector('.mobile-search');

    mobileMenu.addEventListener('click', function() {
        mobileMenu.classList.toggle('active');
        navMenu.classList.toggle('active');
        mobileSearchForm.classList.remove('active');
    });

    mobileSearchIcon.addEventListener('click', function() {
        mobileSearchForm.classList.toggle('active');
        navMenu.classList.remove('active');
        mobileMenu.classList.remove('active');
    });

    // Close mobile menu and search when a nav item is clicked
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            mobileMenu.classList.remove('active');
            navMenu.classList.remove('active');
            mobileSearchForm.classList.remove('active');
        });
    });
});

function playMovie(movieId) {
    const videoPlayer = document.getElementById('video-player');
    const iframe = videoPlayer.querySelector('iframe');
    
    const videoUrl = `https://vidsrc.vip/embed/movie/${movieId}`;
    
    iframe.src = videoUrl;
    videoPlayer.classList.add('active');
    document.body.style.overflow = 'hidden';
}

function closePlayer() {
    const videoPlayer = document.getElementById('video-player');
    const iframe = videoPlayer.querySelector('iframe');
    
    iframe.src = '';
    videoPlayer.classList.remove('active');
    document.body.style.overflow = '';
}

// Close player when clicking outside the video
document.getElementById('video-player').addEventListener('click', function(event) {
    if (event.target === this) {
        closePlayer();
    }
});

// Close player with Escape key
document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
        closePlayer();
    }
});

// Adjust movie content padding on mobile devices
function adjustMovieContentPadding() {
    const header = document.querySelector('header');
    const movieContent = document.querySelector('.movie-content');
    
    if (window.innerWidth <= 768) {
        const headerHeight = header.offsetHeight;
        movieContent.style.paddingTop = `${headerHeight + 20}px`;
    } else {
        movieContent.style.paddingTop = '';
    }
}

window.addEventListener('load', adjustMovieContentPadding);
window.addEventListener('resize', adjustMovieContentPadding);
