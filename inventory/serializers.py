from dataclasses import fields
from rest_framework import serializers
from . models import Category,Item


# Serializers define the API representation.
# class ItemSerializer(serializers.ModelSerializer):
#     item_category = serializers.RelatedField(source='Category', read_only=True)

#     class Meta:
#         model = Item
#         fields = ['id','item_name','description','item_state','item_category','item_image','item_tag']


# class CategorySerializer(serializers.ModelSerializer):
#      items_cat = ItemSerializer(read_only = True,many=True)
#     class Meta:
#         model = Category
#         fields = ['id','name']




class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    items_cat = ItemSerializer(read_only = True,many=True)
    class Meta:
        model = Category
        fields = '__all__'