from rest_framework import serializers
from rest_framework.authtoken.models import Token
from todos import models


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
        )

        model = models.Todo


