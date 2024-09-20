

$(document).ready(function () {
    // Initially show all elements and buttons
    $('.toggle-elements').show();
    $('#hide-btn').show();
    $('#show-btn').hide();

    // Function to show elements
    function showElements() {
        $('.toggle-elements').show();
        $('#show-btn').hide();
        $('#hide-btn').show();
    }

    // Function to hide elements
    function hideElements() {
        $('.toggle-elements').hide();
        $('#hide-btn').hide();
        $('#show-btn').show();
    }

    // Click event for the show button
    $('#show-btn').click(showElements);

    // Click event for the hide button
    $('#hide-btn').click(hideElements);
});

//=========================================================================================================\\

$(document).ready(function () {
    $('.delete-all').click(function () {
        alert("Delete All?");
    });
});

//==========================================================================================================\\

// Get the button element
const scrollToTopBtn = document.getElementById('scrollToTopBtn');

// Show the button when the user scrolls down 100px from the top of the document
window.onscroll = function () {
    if (document.body.scrollTop > 200 || document.documentElement.scrollTop > 100) {
        scrollToTopBtn.classList.add('show');
    } else {
        scrollToTopBtn.classList.remove('show');
    }
};

// Scroll to the top of the page when the button is clicked
scrollToTopBtn.onclick = function () {
    window.scrollTo({ top: 0, behavior: 'smooth' });
};

//==========================================================================================================\\


document.addEventListener('DOMContentLoaded', function () {
    const scrollToTopBtn = document.getElementById('scrollToTopBtn');

    // Show or hide the button based on scroll position
    window.addEventListener('scroll', function () {
        if (window.scrollY > 200) { // Adjust the threshold as needed
            scrollToTopBtn.style.display = 'block';
            scrollToTopBtn.classList.add('bounce'); // Add bounce effect
        } else {
            scrollToTopBtn.style.display = 'none';
            scrollToTopBtn.classList.remove('bounce'); // Remove bounce effect
        }
    });

    // Scroll to the top when the button is clicked
    scrollToTopBtn.addEventListener('click', function () {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
});

//==========================================================================================================\\

$(document).ready(function () {
    // Initially hide the elements
    $(".show-grid").hide();
    $(".btn-hide").hide();
    $(".btn-show").show();

    // Show the grid and toggle buttons when the "Show" button is clicked
    $(".btn-show").click(function () {
        $(".show-grid").show();
        $(".btn-hide").show();
        $(".btn-show").hide();
    });

    // Hide the grid and toggle buttons when the "Hide" button is clicked
    $(".btn-hide").click(function () {
        $(".show-grid").hide();
        $(".btn-hide").hide();
        $(".btn-show").show();
    });
});

//==========================================================================================================\\

