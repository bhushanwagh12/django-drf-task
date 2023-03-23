from rest_framework import serializers
from rest_framework.serializers import Serializer
from .models import Product, ProductImage

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('product_image')


class ProductSerializer(serializers.ModelSerializer):
    nested_data = ProductImageSerializer(many=True)
    class Meta:
        model = Product
        fields = '__all__'