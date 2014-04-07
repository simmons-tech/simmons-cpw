import json
from django.utils import timezone

from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder


# Create your views here.

from tours.models import TourRequest


def get_latest_request():
    if TourRequest.objects.count() == 0:
        return None
    return TourRequest.objects.order_by('-request_time')[0]

# response_data is a dictionary to be returned as json
def json_response(response_data):
    return HttpResponse(json.dumps(response_data, cls=DjangoJSONEncoder), content_type='application/json')

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

