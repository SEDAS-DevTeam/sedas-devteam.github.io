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
})