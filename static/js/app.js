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

$(function() {
    $('asdfbutton').click(function() {
        var summ = $('#summonerInput').val();
        $.ajax({
            url: '/lookup',
            type: 'GET',
            data: $('form').serialize(),
            success: function(response) {
                console.log(response)
                
            },
            error: function(error) {
                console.log(error)
            }
        });
    });
});
    /*
$.ajax({
        url: "/lookup",
        type: "POST",
        data: {},
        success: function(response){
            console.log("yay");
        }
})
    .fail(function() {
        console.log("fail");
    })
    .always(function() {
    });
*/
