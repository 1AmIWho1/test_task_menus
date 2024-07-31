from django.shortcuts import render, redirect

# Create your views here.

from .models import Menu


def index(request):
    return redirect('menu')


def menu(request, menu_name=None):
    context = {'menu_name': menu_name}
    return render(request, 'menu.html', context)


def menus(request):
    roots = Menu.objects.filter(parent_menu=None)
    context = {'roots': roots}
    return render(request, 'menus.html', context)
