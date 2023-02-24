
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from inventory.views import CategoryView, ItemListView,ItemDetailView,CategoryDetailView


# router = routers.DefaultRouter()
# router.register(r'items', ItemListView)
# router.register(r'category', CategoryView)  



urlpatterns = [
    # path('', include(router.urls)),
    path('items/',ItemListView.as_view(),name='itemlist'),
    path('category/',CategoryView.as_view(),name='category'),
    path('items/<int:pk>/', ItemDetailView.as_view(),name='item_detail'),
    path('category/<int:pk>/', CategoryDetailView.as_view(),name='cat_detail'),
]
