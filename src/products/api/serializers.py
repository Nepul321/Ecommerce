from rest_framework import serializers
from ..models import Product


class ProductSerializer(serializers.ModelSerializer):
    image1 = serializers.SerializerMethodField(read_only=True)
    image2 = serializers.SerializerMethodField(read_only=True)
    image3 = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'price', 'digital', 'main_image', 'image1', 'image2', 'image3')

    def get_image1(self, obj):
        image_url = None
        if obj.image1:
            image_url = obj.image1.url
        return image_url

    def get_image2(self, obj):
        image_url = None
        if obj.image2:
            image_url = obj.image2.url
        return image_url

    def get_image3(self, obj):
        image_url = None
        if obj.image3:
            image_url = obj.image3.url
        return image_url