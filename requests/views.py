from rest_framework import viewsets

from requests import models, serializers


class UserRequestViewSet(viewsets.ModelViewSet):
    queryset = models.UserRequest.objects.all()
    serializer_class = serializers.UserRequestSerializer
