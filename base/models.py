from django.db import models

# Create your models here.
class fileupload(models.Model):
    file = models.FileField()
    information = models.CharField(max_length=255, blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    approved = models.BooleanField(default=False)
    recommendation = models.CharField(max_length=255, blank=True, null=True)
    
