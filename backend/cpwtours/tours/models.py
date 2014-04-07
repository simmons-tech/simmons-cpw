from django.db import models
from datetime import datetime

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

    request_time = models.DateTimeField(auto_now_add=True)
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
        self.claim_time = datetime.now()
        self.status = TourRequest.CLAIMED
        self.save()

    def start_tour(self):
        if self.status == TourRequest.REQUESTED:
            self.claime_time = datetime.now()
        if self.status == TourRequest.STARTED:
            raise ValueError("Latest tour request already started")
        self.start_time = datetime.now()
        self.status = TourRequest.STARTED
        self.save()
