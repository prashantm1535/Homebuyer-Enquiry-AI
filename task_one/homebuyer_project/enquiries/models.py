from django.db import models

class Enquiry(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    income = models.FloatField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    property_type = models.CharField(max_length=100, blank=True, null=True)
    budget = models.FloatField(blank=True, null=True)
    followups = models.IntegerField(blank=True, null=True)
    site_visited = models.BooleanField(default=False)
    booked = models.BooleanField(default=False)
    interested = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.city}"
