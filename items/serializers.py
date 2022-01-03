from rest_framework import serializers

from items import models


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ItemImage
        fields = ['id', 'image']


class ItemSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, required=False)

    class Meta:
        model = models.Item
        fields = ['id', 'name', 'description', 'price', 'in_stock', 'images']
