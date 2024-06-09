document.addEventListener('DOMContentLoaded', () => {
    const spans = document.querySelectorAll('.hero-h1-span');
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

    // Handle form submission
    $('#loginForm').submit(function(e) {
        e.preventDefault();
        var form = $(this);
        var url = form.attr('action');
        var formData = form.serialize();

        $.post(url, formData)
            .done(function(response) {
                // Assuming your backend returns a JSON response with a 'success' field
                if (response.success) {
                    // Redirect to home page or perform any other action
                    window.location.href = "{% url 'home' %}";
                } else {
                    // Display error message or handle accordingly
                    alert("Login failed. Please try again.");
                }
            })
            .fail(function() {
                alert("An error occurred. Please try again later.");
            });
    });
});