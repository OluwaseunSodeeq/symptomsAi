document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('.search').addEventListener('click', function(){
       
        document.querySelector('.search-bar').classList.toggle('show');
        document.querySelector('.header-img').classList.toggle('hide');
    });
});

document.addEventListener("DOMContentLoaded", function() {
    function updatePlaceholder() {
        var screenWidth = window.innerWidth;
        var inputElement = document.querySelector('.input-text textarea');

        if (screenWidth <= 576) { 
            if (inputElement) inputElement.placeholder = ' ';
        } else {
            if (inputElement) inputElement.placeholder = 'Enter your symptoms...';
        }
    }

    // Run on initial load
    updatePlaceholder();

    // Run on window resize
    window.addEventListener('resize', updatePlaceholder);
});

