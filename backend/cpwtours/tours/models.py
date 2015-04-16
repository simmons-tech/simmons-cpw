from django.db import models
from django.utils import timezone

# Create your models here.

class TourRequest(models.Model):
    REQUESTED = 'R'
    CLAIMED = 'C'
    STARTED = 'S'
    STATUS_CHOICES = (
        (REQUESTED, 'Requested'),
        (CLAIMED, 'Claimed'),
        (STARTED, 'Started'),
    )
    
    status = models.CharField(max_length = 1,
                              choices = STATUS_CHOICES,
                              default = REQUESTED)

    request_time = models.DateTimeField()
    claim_time = models.DateTimeField(blank=True, null = True, default = None)
    start_time = models.DateTimeField(blank=True, null = True, default = None)
    
    def is_unclaimed(self):
        return self.status == TourRequest.REQUESTED

    def is_started(self):
        return self.status == TourRequest.STARTED
    
    def claim_tour(self):
        if self.status == TourRequest.CLAIMED:
            raise ValueError("Latest tour already claimed")
        if self.status == TourRequest.STARTED:
            raise ValueError("Latest tour already started")
        self.claim_time = timezone.now()
        self.status = TourRequest.CLAIMED
        self.save()

    def start_tour(self):
        if self.status == TourRequest.REQUESTED:
            self.claim_time = timezone.now()
        if self.status == TourRequest.STARTED:
            raise ValueError("Latest tour request already started")
        self.start_time = timezone.now()
        self.status = TourRequest.STARTED
        self.save()

    def time_to_str(self, dt):
        if not dt:
            return None
        return timezone.localtime(dt).strftime("%a %I:%M%p")

    def to_json(self):
        response_data = {}
        response_data['status'] = self.status
        response_data['request_time'] = self.time_to_str(self.request_time)
        response_data['claim_time'] = self.time_to_str(self.claim_time)
        response_data['start_time'] = self.time_to_str(self.start_time)
        response_data['id'] = self.id
        return response_data
        

    def __str__(self):
        return "Tour Request - %s [%s]" % (self.time_to_str(self.request_time), self.get_status_display())
