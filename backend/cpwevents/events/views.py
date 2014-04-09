import json

from django.shortcuts import render
from django.utils import timezone

from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.core.mail import send_mail

from events.models import CpwEvent

def localtime_now():
    return timezone.localtime(timezone.now())

# Returns QuerySet showing events that just finished
# in order of decreasing end time. 
def events_just_finished():
    return CpwEvent.objects.filter(end_time__lt=localtime_now()).order_by('-end_time')

# Returns QuerySet with events currently happening
# in increasing start time.
def events_happening_now():
    return CpwEvent.objects.filter(start_time__lt=localtime_now()).filter(end_time__gt=localtime_now()).order_by('start_time')

# Returns QuerySet with events that haven't started yet
# sorted by increasing start time.
def upcoming_events():
    return CpwEvent.objects.filter(start_time__gt=localtime_now()).order_by('start_time')

# response_data is a dictionary to be returned as json
def json_response(response_data):
    return HttpResponse(json.dumps(response_data, cls=DjangoJSONEncoder, indent=4), content_type='application/json')

# Views
def info(request):
    happening_now = [evt.to_json() for evt in events_happening_now()]
    upcoming = [evt.to_json() for evt in upcoming_events()]
    past = [evt.to_json() for evt in events_just_finished()]

    response_data = {}
    response_data['now_date'] = CpwEvent.date_str(localtime_now())    
    response_data['now_time'] = CpwEvent.time_str(localtime_now())
    response_data['happening_now'] = happening_now
    response_data['upcoming'] = upcoming
    response_data['recently_ended'] = past

    return json_response(response_data)

