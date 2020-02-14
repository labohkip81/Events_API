from rest_framework import serializers
from todos import models
from Events.models import EventsDetails


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
        )

        model = models.Todo

    

        

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'name',
            'user',
            'event_date',
            'event_start_time',
            'event_end_time',
            'image_url',
            'event_type_id',
            'event_url',
            'event_description',
            'status',
            'created_at',
            'updated_at',

        )
        model = EventsDetails




    # name = models.TextField(max_length=100)
    # #category_id = models.ForeignKey(Category)
    # user = models.ForeignKey(User, models.CASCADE)
    # event_date = models.DateTimeField()
    # event_start_time = models.DateTimeField()
    # event_end_time = models.DateTimeField()
    # image_url = models.URLField()
    # event_type_id = models.CharField(default=uuid.uuid4, max_length=256)
    # event_url = models.URLField()
    # event_description = models.TextField(max_length=256)
    # status = models.BooleanField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now_add=True)
