 // Text animation hero section
 document.addEventListener('DOMContentLoaded', () => {
    const spans = document.querySelectorAll('#hero-h1-span');
    spans.forEach((span, index) => {
        setTimeout(() => {
            span.classList.add('visible');
        }, index * 400); // Adjust the delay time as needed
    });
});


$(document).ready(function() {
    // Trigger login modal
    $('a[data-bs-target="#loginModal"]').click(function(e) {
        e.preventDefault();
        $('#loginModal').modal('show');
    });

    // Trigger signup modal (assuming the button has the class "signup-button")
    $('.signup-button').click(function(e) {
        e.preventDefault();
        $('#signupModal').modal('show');
    });
});