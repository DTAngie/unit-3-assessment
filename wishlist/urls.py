from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('items/create/', views.ItemCreate.as_view(), name="item_create" ),
]