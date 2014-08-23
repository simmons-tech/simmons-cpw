var TOUR_REQUEST_URL = "http://simmons-hall.scripts.mit.edu/frosh/backend/cpwtours/tours/request"
var TOUR_START_URL = "http://simmons-hall.scripts.mit.edu/frosh/backend/cpwtours/tours/start"
var INFO_URL = "http://simmons-hall.scripts.mit.edu/frosh/backend/cpwtours/tours/info"
var EVENT_URL = "http://simmons-hall.scripts.mit.edu/frosh/backend/cpwevents/events"

var REQUESTED = "R";
var CLAIMED = "C";
var STARTED = "S";

$(document).ready(function() {
    var eventTemplate = _.template($("#event-template").html());
    var tourRequested = false;

    var errorP = $('#error-msg');

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

    var sendTourRequest = function(url) {
	$.getJSON(url)
	.done(function(json) {
	    checkResponse(json);
	})
	.fail(showGetJsonError);
    };

    // Setup request commands. Just getting these urls will change the status.
    var requestTour = function() {
	   sendTourRequest(TOUR_REQUEST_URL);
    };

    var startTour = function() {
	   sendTourRequest(TOUR_START_URL);
    };


    // Display error message in red.
    var displayError = function(msg) {
	   errorP.text(msg);
    };

    var updateToursDisplay = function(json) {
        displayError("");
        var latest_request = json['latest_request'];
        var numRequests = json['num_requests']

        if (!latest_request || latest_request['status'] == STARTED) {
            $("#tour-status-text").text("Last tour started:");
            $("#tour-time").text(latest_request['start_time']);
            $("#tour-requested").addClass("hidden")
            $("#tour-top-text").text("Talk to the desk worker to request a tour.");
            tourRequested = false;
        } else if (latest_request['status'] == REQUESTED) {
            $("#tour-status-text").text("Tour requested:");
            $("#tour-time").text(latest_request['request_time']);
            $("#tour-requested").removeClass("hidden");
            $("#tour-top-text").text("Thanks for requeting a tour! Feel free to wait in our mailbox lounge.");
            tourRequested = true;
        } else if (latest_request['status'] == CLAIMED) {
            $("#tour-status-text").text("Tour claimed:");
            $("#tour-time").text(latest_request['claim_time']);
            $("#tour-requested").removeClass("hidden");
            $("#tour-top-text").text("Your request has been claimed by a guide. We'll leave shortly.");
            tourRequested = true;
        }
    }
    var updateEventsDisplay = function(json) {
        $("#event-wrapper").html("");
        $("#now").html(json['now_date'] +' &nbsp;&nbsp;&nbsp; ' + json['now_time']);

        if (json['happening_now'].length > 0) {
            $("#happening-text").text("Happening now:");
            for (var i = 0; i < json['happening_now'].length; i++) {
                $("#event-wrapper").append(eventTemplate(json['happening_now'][i]));
            }
        } else if (json['upcoming'].length > 0) {
            $("#happening-text").text("Starting soon:");
            $("#event-wrapper").append(eventTemplate(json['upcoming'][0]));
            $("#event-wrapper").append(eventTemplate(json['upcoming'][1]));
        } else {
            $("#happening-text").text("That's all! See you in the fall");
        }
    }

    var loadEvents = function() {
        $.getJSON(EVENT_URL)
        .done(function(json) {
	    updateEventsDisplay(json);
        })
	   .fail(showGetJsonError);
    }
    var loadTours = function() {
        $.getJSON(INFO_URL)
        .done(function(json) {
	    updateToursDisplay(json);
        })
	   .fail(showGetJsonError);
    }

    loadEvents();
    setInterval(loadEvents, 30*1000)
});
