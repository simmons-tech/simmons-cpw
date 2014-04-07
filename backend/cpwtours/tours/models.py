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
        return self.status == REQUESTED

    def is_started(self):
        return self.status == STARTED
    
    def claim_tour(self):
        if self.status == CLAIMED:
            raise ValueError("Tour already claimed")
        if self.status == STARTED:
            raise ValueError("Tour already startdd")
        self.claim_time = datetime.now()
        self.status = CLAIMED
        self.save()

    def start_tour(self):
        if self.status == REQUESTED:
            self.claime_time = datetime.now()
        if self.status == STARTED:
            raise ValueError("Tour already startdd")
        self.start_time = datetime.now()
        self.status = STARTED
        self.save()
