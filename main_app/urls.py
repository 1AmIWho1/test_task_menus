from django.urls import path

from . import views

urlpatterns = [
    path('menu/', views.menu, name='menu'),
    path('menu/<menu_name>/', views.menu, name='menu_link'),
    path('menus/', views.menus, name='menus'),
    path('', views.index, name='index'),
]
