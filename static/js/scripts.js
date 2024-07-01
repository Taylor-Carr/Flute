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

document.addEventListener('DOMContentLoaded', function() {
    // Get open modal button
    var openModalBtn = document.getElementById("openModalBtn");
    // Get modal element
    var modal = document.getElementById("customizeFormModal");
    // Get close button
    var closeBtn = document.querySelector(".closeBtn");

    // Check if modal element exists
    if (modal) {
        // Listen for open click
        openModalBtn.addEventListener("click", openModal);

        // Listen for close click
        closeBtn.addEventListener("click", closeModal);

        // Listen for outside click
        window.addEventListener("click", clickOutside);

        // Function to open modal
        function openModal() {
            modal.style.display = "block";
        }

        // Function to close modal
        function closeModal() {
            modal.style.display = "none";
        }

        // Function to close modal if outside click
        function clickOutside(e) {
            if (e.target == modal) {
                modal.style.display = "none";
            }
        }
    } else {
        console.error("Modal element not found.");
    }
});