from django.db import models

# Create your models here.
class FeedbackModel(models.Model):
    name = models.CharField(max_length=100)
    email= models.EmailField()
    phone = models.IntegerField()
    address = models.CharField(max_length=100)
    message = models.TextField()