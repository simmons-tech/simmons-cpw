from django.db import models
from django.utils import timezone

# Create your models here.

class CpwEvent(models.Model):

    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    short_description = models.TextField()    
    
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    @staticmethod
    def date_str(dt):
        if not dt:
            return None
        return timezone.localtime(dt).strftime("%A, %B %d")


    @staticmethod
    def time_str(dt):
        if not dt:
            return None
        return timezone.localtime(dt).strftime("%I:%M%p")

    def to_json(self):
        response_data = {}
        response_data['title'] = self.title
        response_data['location'] = self.location
        response_data['description'] = self.description
        response_data['short_description'] = self.short_description        

        response_data['day'] = CpwEvent.date_str(self.start_time)        
        response_data['start_time'] = CpwEvent.time_str(self.start_time)
        response_data['end_time'] = CpwEvent.time_str(self.end_time)
        response_data['id'] = self.id
        return response_data

    def __str__(self):
        return "%s [%s]" % (self.title, timezone.localtime(self.start_time).strftime("%a. %I:%M%p"))
    
    class Meta:
        verbose_name = 'CPW Event'
