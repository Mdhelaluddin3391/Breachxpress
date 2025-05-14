function toggleMenu() {
    const slideMenu = document.querySelector('.slide-menu');
    const body = document.body;
    slideMenu.classList.toggle('active');
    // Toggle scroll lock
    if (slideMenu.classList.contains('active')) {
        body.classList.add('no-scroll');
    } else {
        body.classList.remove('no-scroll');
    }
}

