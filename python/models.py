from django.db import models

class Process(models.Model):
    process_id = models.PositiveIntegerField()
    arrival_time = models.FloatField()
    burst_time = models.FloatField()
    waiting_time = models.FloatField()
    turnaround_time = models.FloatField()
    priority = models.FloatField()
    age = models.PositiveIntegerField()
