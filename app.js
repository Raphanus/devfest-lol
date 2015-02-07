(function() {
    var app = angular.module('devFestSite', []);

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
