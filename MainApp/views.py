from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def home(request):
    #text = """
    #<h1>"Изучаем django"</h1>
    #<strong>Автор</strong>: <i>Иванов И.П.</i>
    #"""
    #return HttpResponse(text)
    context = {
        "name": "Цабенко Максим Валерьевич",
        "email": "max800@mail.ru",
    }
    return render(request, "index.html", context)

def about(request):
    author = {
    "name": "Максим",
    "middle_name": "Валерьевич",
    "last_name": "Цабенко",
    "phone": "8-919-723-15-74",
    "email": "max800@mail.ru"
    }
    return render(request, "about.html", {"author": author})
    

def get_item(request, item_id: int):
    """ По указанному id возвращаем элемент из БД"""
    try:
        item = Item.objects.get(id=item_id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f"Item with id={item_id} not found")
    else:
        context = {"item": item}
        return render(request, "item_page.html", context)
    

def get_items(request):
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request, "items_list.html", context)