from django import template
from django.utils.safestring import mark_safe

from ..models import Menu


register = template.Library()


def inner_list(menus, menu):
    res = f'<li><a href="/menu/{menu.name}"><h2>{menu.name}</h2></a>'
    res += '<ul>'
    for menu_child in menus:
        if menu_child.name != menu.name and menu_child.parent_menu == menu:
            res += f'<li><a href="/menu/{menu_child.name}">{menu_child.name}</a></li>'
    res += '</ul></li>'
    return res


def recursion(root, menus, depth, menu):
    res = ''
    menu_children = menus.filter(parent_menu=root)
    if depth == 1:
        
        res += f'<li><a href="/menu/{root.name}">{root.name}</a><ul>'
        for menu_child in menu_children:
            if menu_child == menu:
                res += inner_list(menus, menu)
            else:
                res += f'<li><a href="/menu/{menu_child.name}">{menu_child.name}</a></li>'
        res += '</ul></li>'
        return res
    res = f'<li><a href="/menu/{root.name}">{root.name}</a><ul>'
    for menu_child in menu_children:
        res += recursion(menu_child, menus, depth - 1, menu)
    res += '</ul></li>'
    return res


def get_all_lists(menu, menus, depth, root):
    if root == menu:
        return '<ul>' + inner_list(menus, menu) + '</ul>'
    if not depth:
        return f'<ul><li><a href="/menu/{root.name}">{root.name}</a></li></ul>'
    return '<ul>' + recursion(root, menus, depth, menu) + '</ul>'


@register.simple_tag
def draw_menu(*args, **kwargs):
    menu_name = args[0]
    menus = Menu.objects.all()
    menu = menus.filter(name=menu_name).first()
    if menu is None:
        return mark_safe('<h1>this menu does not exist!</h1>')

    depth = 0
    root = menu
    while root.parent_menu is not None:
        root = root.parent_menu
        depth += 1

    return mark_safe(get_all_lists(menu, menus, depth, root))
