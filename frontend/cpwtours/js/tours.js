var BASE_URL = "http://127.0.0.1:8000/tours"
var INFO_URL = BASE_URL + "/info"

$(document).ready(function() {
    
    var loadData = function() {
        $.getJSON(INFO_URL)
        .done(function(json) {
            console.log(json);
        })
        .fail(function (jqxhr, textStatus, error) {
            var err = textStatus + ", " + error;
            console.log("Request Failed: " + err);
        });
    }
    
    var initApp = function() {
        loadData();
    }
    
    initApp();
});