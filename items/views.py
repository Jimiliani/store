from rest_framework import viewsets

from items import serializers, models


class ItemViewSet(viewsets.ModelViewSet):
    queryset = models.Item.objects.all().order_by('-in_stock', 'id')
    serializer_class = serializers.ItemSerializer
