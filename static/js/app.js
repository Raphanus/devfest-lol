(function() {
    //var app = angular.module('devFestSite', []);

    console.log("test");
    $.ajax({
            url: "/data.py",
            type: "POST",
            data: {},
            success: function(response){
                console.log("yay");
            }
    });






})
console.log('test1');

$.ajax({
        url: "data.py",
        type: "POST",
        data: {},
        success: function(response){
            console.log("yay");
        }
})
    .fail(function() {
        console.log(url);
    })
    .always(function() {
    });

