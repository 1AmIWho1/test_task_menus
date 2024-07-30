from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    return redirect('menu')


def menu(request, menu_name=None):
    context = {'menu_name': menu_name}
    return render(request, 'menu.html', context)
