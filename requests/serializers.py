from rest_framework import serializers

from requests import models


class UserRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserRequest
        fields = ['id', 'name', 'phone', 'email']
