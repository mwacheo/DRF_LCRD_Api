
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls


router = DefaultRouter()
schema_view = get_schema_view(title='Inventory API',
                description='An API to Add Items and its categories.')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inventory.urls')),
    path('schema/', schema_view),
    path('docs/', include_docs_urls(title='Inventory API'))
]
