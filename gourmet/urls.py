from django.urls import path
from . import views

app_name = 'gourmet'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:restaurant_id>/', views.detail, name='detail'),
]
