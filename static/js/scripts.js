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


// Function to check if an element is in viewport
function isInViewport(element) {
    const rect = element.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}

// Function to add animation class with delay when element is in viewport
function addAnimationOnScroll() {
    const cards = document.querySelectorAll('#service-card');

    cards.forEach((card, index) => {
        if (isInViewport(card)) {
            // Calculate delay based on index
            const delay = index * 100; // Adjust delay timing (200ms between each card)

            // Add animation class with delay
            setTimeout(() => {
                card.classList.add('animate');
            }, delay);
        }
    });
}

// Initial check on page load
document.addEventListener('DOMContentLoaded', addAnimationOnScroll);

// Listen for scroll events and check visibility of service cards
window.addEventListener('scroll', addAnimationOnScroll);

//form toggle image upload 

function toggleLogoOptions() {
    var uploadLogoInput = document.getElementById('id_logo_image');
    var uploadLogoRadio = document.getElementById('upload_logo');
    var useCompanyNameRadio = document.getElementById('use_company_name');

    if (uploadLogoRadio.checked) {
        uploadLogoInput.style.display = 'block';
    } else {
        uploadLogoInput.style.display = 'none';
    }
}

function toggleImageOptions() {
    var ownImagesInput = document.getElementById('id_upload_images');
    var ownImagesRadio = document.getElementById('use_own_images');
    var stockImagesRadio = document.getElementById('use_stock_images');

    if (ownImagesRadio.checked) {
        ownImagesInput.style.display = 'block';
    } else {
        ownImagesInput.style.display = 'none';
    }
}