from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.



class EventsDetails(models.Model):
    name = models.TextField(max_length=100)
    #category_id = models.ForeignKey(Category)
    user = models.ForeignKey(User, models.CASCADE)
    event_date = models.DateTimeField()
    event_start_time = models.DateTimeField()
    event_end_time = models.DateTimeField()
    image_url = models.URLField()
    event_type_id = models.CharField(default=uuid.uuid4, max_length=256)
    event_url = models.URLField()
    event_description = models.TextField(max_length=256)
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)



