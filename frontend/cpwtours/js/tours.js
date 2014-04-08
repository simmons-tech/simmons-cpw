var BASE_URL = "/cpw/backend/cpwtours/tours"
var INFO_URL = BASE_URL + "/info"
var REQUEST_URL = BASE_URL + "/request"
var CLAIM_URL = BASE_URL + "/claim"
var START_URL = BASE_URL + "/start"

var REQUESTED = "R";
var CLAIMED = "C";
var STARTED = "S";

$(document).ready(function() {
    var errorP = $('#error-msg');
    var tourNumSpans = $('.tour-num');

    // Four "states" of the page
    var noDataDiv = $('#no-data');    
    var noRequestsDiv = $('#no-requests');
    var unclaimedDiv = $('#unclaimed-request');
    var unstartedDiv = $('#unstarted-request');

    // Handle AJAX JSON Responses
    var showGetJsonError = function (jqxhr, textStatus, error) {
            var err = textStatus + ", " + error;
	    displayError("Request failed: " + err);
    };

    var checkResponse = function (json) {
	if(json['success']) {
	    // Success
	    location.reload();
	} else {
	    displayError(json['message']);
	}
    };

    var sendRequest = function(url) {
	$.getJSON(url)
	.done(function(json) {
	    checkResponse(json);
	})
	.fail(showGetJsonError);
    };

    // Setup request commands. Just getting these urls will change the status.
    var requestTour = function() {
	sendRequest(REQUEST_URL);
    };
    var claimTour = function() {
	sendRequest(CLAIM_URL);
    };
    var startTour = function() {
	sendRequest(START_URL);
    };

    // Link to buttons
    $("#request_tour_btn").click(function() {
	requestTour();
    });
    $("#unclaimed_claim_tour_btn").click(function() {
	claimTour();
    });
    $("#unclaimed_start_tour_btn").click(function() {
	startTour();
    });
    $("#unstarted_start_tour_btn").click(function() {
	startTour();
    });


    // Display error message in red.
    var displayError = function(msg) {
	errorP.text(msg);
    };

    var updateDisplay = function(json) {
	displayError("");
	var latest_request = json['latest_request'];
	var numRequests = json['num_requests']

	noDataDiv.addClass("hidden");	
	noRequestsDiv.addClass("hidden");
	unclaimedDiv.addClass("hidden");
	unstartedDiv.addClass("hidden");

	if (!latest_request || latest_request['status'] == STARTED) {
	    noRequestsDiv.removeClass("hidden");

	    if (latest_request) {
		$('#latest_start_time').text(latest_request['start_time']);
	    }
	    // This will be tour (num_so_far + 1)
	    numRequests += 1;
	} else if (latest_request['status'] == REQUESTED) {
	    $('#unclaimed_request_time').text(latest_request['request_time']);	    
	    unclaimedDiv.removeClass("hidden");	    
	} else if (latest_request['status'] == CLAIMED) {
	    $('#unstarted_request_time').text(latest_request['request_time']);
	    $('#unstarted_claim_time').text(latest_request['claim_time']);	    	    	    
	    unstartedDiv.removeClass("hidden");	    	    
	}
	
	tourNumSpans.text(numRequests);
    }
    
    var loadData = function() {
        $.getJSON(INFO_URL)
        .done(function(json) {
	    updateDisplay(json);
        })
	.fail(showGetJsonError);
    }
    
    var initApp = function() {
        loadData();
    }

    initApp();
    setInterval(initApp, 5*1000)
});
