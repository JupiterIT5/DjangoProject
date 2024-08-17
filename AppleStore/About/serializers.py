from rest_framework import serializers
from About.models import *
from django import forms


class ProductSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(label='Цена', max_digits=10, decimal_places=2)

    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price',
            'create_date',
            'update_date',
            'photo',
            'is_exists',
            'warehouse',
            'parametr',
            'category',
            'tag',
        ]


class ProductSerializerSimple(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price',
        ]


class ParametrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parametr
        fields = [
            'name'
        ]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            'name',
            'description'
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name',
            'description'
        ]
