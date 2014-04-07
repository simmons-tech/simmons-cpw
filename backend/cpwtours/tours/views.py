import json

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from tours.models import TourRequest

def info(request):
    response_data = {}
    response_data['result'] = 'Tour Info'
    response_data['message'] = 'The message'
    return HttpResponse(json.dumps(response_data), content_type='application/json')

def request_tour(request):
    response_data = {}
    response_data['result'] = 'Request Tour'
    response_data['message'] = 'The message'
    return HttpResponse(json.dumps(response_data), content_type='application/json')

def claim_tour(request):
    response_data = {}
    response_data['result'] = 'Claim tour'
    response_data['message'] = 'The message'
    return HttpResponse(json.dumps(response_data), content_type='application/json')

def start_tour(request):
    response_data = {}
    response_data['result'] = 'Start tour'
    response_data['message'] = 'The message'
    return HttpResponse(json.dumps(response_data), content_type='application/json')

