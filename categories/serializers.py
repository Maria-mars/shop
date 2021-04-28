from rest_framework import serializers
from categories.models import Category
#from .models import models

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'objects', 'name', 'slug', 'created_at', 'updated_at',)
        model = Category
