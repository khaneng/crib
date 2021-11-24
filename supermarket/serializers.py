from .models import Category,Items
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name','is_sub_category']

class ItemSerializer(serializers.ModelSerializer):
    # category = CategorySerializer(many=True, read_only=True)
    category_name = serializers.CharField(source='category.name', required = False)
    sub_category_name = serializers.CharField(source='sub_category.name', required = False)
    class Meta:
        model = Items
        fields = ['name','category','category_id','sub_category','category_name','sub_category_name']