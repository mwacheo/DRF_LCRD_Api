from unicodedata import category
from django.shortcuts import get_object_or_404, render
from rest_framework import generics,status
from . import serializers
from . models import Category, Item
from rest_framework.response import Response


# # ViewSets define the view behavior.
# class ItemListView(generics.GenericAPIView):
#     queryset = Item.objects.all()
#     serializer_class = serializers.ItemSerializer   

# #ItemList
#     def get(self,request):
#         items = Item.objects.all()
#         serializer = self.serializer_class(instance=items,many=True)
#         return Response(data=serializer.data,status=status.HTTP_200_OK)

# #Add Item
#     def post(self,request):
#         data=request.data
#         serializer = self.serializer_class(data=data)


#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data,status=status.HTTP_201_CREATED)
#         return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# #Get Item By ID
# class ItemDetailView(generics.GenericAPIView):
#     queryset = Item.objects.all()
#     serializer_class = serializers.ItemSerializer   

#     def get(self,request,item_id):
#         items = get_object_or_404(Item,pk=item_id)
#         serializer = self.serializer_class(instance=items)
#         return Response(data=serializer.data,status=status.HTTP_200_OK)


# #Edit An Item By ID
# #   
#     def put(self,request,item_id):
#         data = request.data
#         items = get_object_or_404(Item,pk=item_id)
#         serializer = self.serializer_class(data=data,instance=items)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data,status=status.HTTP_200_OK)
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# #Delete An Item
  
#     def delete(self,request,item_id):
#         items = get_object_or_404(Item,pk=item_id)
#         items.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# ##################################################################################################################################################################################################
    

# class CategoryView(generics.GenericAPIView):
#     queryset = Category.objects.all()
#     serializer_class = serializers.CategorySerializer

#     #CategoryList
#     def get(self,request):
#         category = Category.objects.all()
#         serializer = self.serializer_class(instance=category,many=True)
#         return Response(data=serializer.data,status=status.HTTP_200_OK)

#     #Add Category
#     def post(self,request):
#         data=request.data
#         serializer = self.serializer_class(data=data)


#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data,status=status.HTTP_201_CREATED)
#         return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# #Get Category By ID
# class CategoryDetailView(generics.GenericAPIView):
#     queryset = Category.objects.all()
#     serializer_class = serializers.CategorySerializer   

#     def get(self,request,cat_id):
#         category = get_object_or_404(Category,pk=cat_id)
#         serializer = self.serializer_class(instance=category)
#         return Response(data=serializer.data,status=status.HTTP_200_OK)


# #Edit An Category By ID
# #   
#     def put(self,request,cat_id):
#         data = request.data
#         category = get_object_or_404(Category,pk=cat_id)
#         serializer = self.serializer_class(data=data,instance=category)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data,status=status.HTTP_200_OK)
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# #Delete Category
  
#     def delete(self,request,cat_id):
#         category = get_object_or_404(Category,pk=cat_id)
#         category.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)




# List and Create Items
class ItemListView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = serializers.ItemSerializer   


#RUD Item By ID
class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = serializers.ItemSerializer  



# List and Create Categories
class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer


#RUD Category By ID
class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer  