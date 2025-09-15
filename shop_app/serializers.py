from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        Model=Product
        fields= ['id', 'name', 'slug', 'image', 'description', 'category', 'price']

        