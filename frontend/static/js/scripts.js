

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


//===========================================================================================================\\

$(document).ready(function () {
    $('.delete-all').click(function () {
        alert("Delete All?");
    });
});

