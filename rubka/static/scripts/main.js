$(document).ready(function () { // большие баннеры на главной
    const slider = $("#slider").owlCarousel({
        loop: true,
        margin: 20,
        nav: true,
        touchDrag: true,
        nav: false,
        dots: true,
        responsive: {
            0: {
                items: 1
            },
            1191: {
                items: 1
            },
        }
    });
});

$(document).ready(function () { // слайдер с аниме тайтлами
    const slider = $("#anime_slider").owlCarousel({
        loop: false,
        margin: 20,
        nav: true,
        touchDrag: true,
        nav: false,
        dots: true,
        responsive: {
            0: {
                items: 3
            },
            1191: {
                items: 5
            },
        }
    });
});

$(document).ready(function () {
    const slider = $("#serial_slider").owlCarousel({
        loop: false,
        margin: 20,
        nav: true,
        touchDrag: true,
        nav: false,
        dots: true,
        responsive: {
            0: {
                items: 3
            },
            1191: {
                items: 5
            },
        }
    });
});

$(document).ready(function () {
    const slider = $("#all_series_slider").owlCarousel({
        loop: false,
        margin: 20,
        nav: true,
        touchDrag: true,
        nav: false,
        dots: true,
        responsive: {
            0: {
                items: 3
            },
            1191: {
                items: 5
            },
        }
    });
});

$(document).ready(function () {
    const slider = $("#podcast_slider").owlCarousel({
        loop: false,
        margin: 20,
        nav: true,
        touchDrag: true,
        nav: false,
        dots: true,
        responsive: {
            0: {
                items: 3
            },
            1191: {
                items: 5
            },
        }
    });
});