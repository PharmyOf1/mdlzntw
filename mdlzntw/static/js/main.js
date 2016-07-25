var Atlanta = global_points[0];
var Portland = global_points[1];
var Richmond = global_points[2];
var Fairlawn = global_points[3];
var Chicago = global_points[4];
var Naperville = global_points[5];
var Salinas = global_points[6];
var Monterrey = global_points[7];
var EastYork = global_points[8];
var Scarborough = global_points[9];
var Montreal = global_points[10];


$("#hold_bakery_title").on({
    mouseenter: function () {
        var x = $(this).attr('name');
        window[x].openPopup();

    },
    mouseleave: function () {
        var x = $(this).attr('name');
        window[x].closePopup();
    }
});
