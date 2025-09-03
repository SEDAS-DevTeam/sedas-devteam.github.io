$(document).ready(() => {
    // Preload the home screen
    $("main").load("home.html");

    $("a#changelog").click((event) => {
        event.preventDefault()
        $("main").load("changelog.html");
    })

    $("a#home").click((event) => {
        event.preventDefault()
        $("main").load("home.html");
    })

    $("a#community").click((event) => {
        event.preventDefault()
        $("main").load("community.html");
    })

    const togglerIcon = $('button.navbar-toggler i.fa-bars');

    // When the navbar is shown (expanded)
    $('#navbarSupportedContent').on('show.bs.collapse', function() {
        togglerIcon.removeClass('rotate-neg-90').addClass('rotate-90');
    });

    // When the navbar is hidden (collapsed)
    $('#navbarSupportedContent').on('hide.bs.collapse', function() {
        togglerIcon.removeClass('rotate-90').addClass('rotate-neg-90');
    });
})