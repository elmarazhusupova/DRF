from rest_framework import serializers
from rest_framework.response import Response

from .models import Women, Category


# class WomenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
