import json
from django.utils import timezone

from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.core.mail import send_mail

from tours.models import TourRequest

# Query Helper
def get_latest_request():
    if TourRequest.objects.count() == 0:
        return None
    return TourRequest.objects.order_by('-request_time')[0]

# response_data is a dictionary to be returned as json
def json_response(response_data):
    return HttpResponse(json.dumps(response_data, cls=DjangoJSONEncoder), content_type='application/json')

# Messages

def request_count():
    return TourRequest.objects.count()

def send_request_email(new_request):
    request_time = new_request.time_to_str(new_request.request_time)
    subject =  "[CPW Tours] Tour #%s Requested" % str(request_count())
    message = "A tour was requested at [%s]. Go to http://simmons-hall.scripts.mit.edu/cpw/tours to claim." % request_time
    send_email_message(subject, message)

def send_claim_email(claimed_request):
    request_time = claimed_request.time_to_str(claimed_request.request_time)
    subject =  "[CPW Tours] Tour #%s Claimed" % str(request_count())
    message =  "The [%s] tour request was claimed. Go to http://simmons-hall.scripts.mit.edu/cpw/tours to view status." % request_time
    send_email_message(subject, message)
    
def send_start_email(started_request):
    request_time = started_request.time_to_str(started_request.request_time)
    subject =  "[CPW Tours] Tour #%s Started" % str(request_count())
    message =  "The  [%s] tour request started. Go to http://simmons-hall.scripts.mit.edu/cpw/tours to view status." % request_time
    send_email_message(subject, message)

def send_email_message(subject, message):
    from_email = "Simmons Tours Website <simmons-tech@mit.edu>"
#    to_emails = ["simmons-cpw-tours-2014@mit.edu"]
    to_emails = ["larsj@mit.edu"]
    send_mail(subject, message, from_email, to_emails, fail_silently=False)

# Views
def info(request):
    num_requests = TourRequest.objects.count()
    latest_request = get_latest_request()

    response_data = {}
    response_data['num_requests'] = num_requests
    response_data['latest_request'] = latest_request.to_json() if latest_request else None
    return json_response(response_data)

def request_tour(request):
    latest_request = get_latest_request()

    if latest_request and not latest_request.is_started():
        success = False
        message = "Last tour hasn't started yet!"
        new_request = None
    else:
        new_request = TourRequest(request_time = timezone.now())
        new_request.save()

        send_request_email(new_request)
        success = True
        message = "Tour successfully requested"
        
    response_data = {}
    response_data['success'] = success
    response_data['message'] = message
    response_data['new_request'] =  new_request.to_json() if new_request else None
    return json_response(response_data)    

def claim_tour(request):
    latest_request = get_latest_request()

    if not latest_request:
        success = False
        message = "No tours requested."
        latest_request = None
    else:
        try:
            latest_request.claim_tour()
            success = True
            message = "Tour successfully claimed"
#            send_claim_email(latest_request)
        except ValueError as e:
            success = False
            message = "Error: " + str(e)

    response_data = {}
    response_data['success'] = success
    response_data['message'] = message
    response_data['latest_request'] =  latest_request.to_json() if latest_request else None
    return json_response(response_data)        

def start_tour(request):
    latest_request = get_latest_request()

    if not latest_request:
        success = False
        message = "No tours requested"
        latest_request = None
    else:
        try:
            latest_request.start_tour()
#            send_start_email(latest_request)
            success = True
            message = "Tour successfully started"
        except ValueError as e:
            success = False
            message = "Error: " + str(e)

    response_data = {}
    response_data['success'] = success
    response_data['message'] = message
    response_data['latest_request'] =  latest_request.to_json() if latest_request else None
    return json_response(response_data)

