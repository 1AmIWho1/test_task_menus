from django.urls import path

from . import views

urlpatterns = [
    path('menu/', views.menu, name='menu'),
    path('menu/<menu_name>/', views.menu, name='menu_link'),
    path('', views.index, name='index'),
]
