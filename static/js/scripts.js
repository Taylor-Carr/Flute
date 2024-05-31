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