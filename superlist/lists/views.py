from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item

# Create your views here.
def home_page(request):
    # return HttpResponse('<html><title>To-Do lists</title><body><h1>To-Do</h1></body></html>')
    # if request.method == 'POST':
    #     return HttpResponse(request.POST['item_text'])

    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])  #.objects.create 是創建新 Item 對象的簡化方式，無須再調用 .save() 方法。
        return redirect('/lists/')

    # else:
    #     new_item_text = ''
    items = Item.objects.all()

    context = {
        'item_text': 'my new item',
        'items': items,
    }
    return render(request, "Lists/home.html", context)

def index(request):
    return HttpResponse("Hello World")