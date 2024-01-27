from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
from django.template import loader

# Create your views here.
def home(request):
    item = Item.objects.all()
    context = {
        'item': item,
    }
    return render(request, 'food/index.html', context)

def item(request):
    return HttpResponse("This is an Item View")

def detail(request, pk):
    item = Item.objects.get(pk=pk)
    context = {
        'item': item
    }
    return render(request, 'food/detail.html', context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('home')

    context={
        'form': form,
    }

    return render(request, 'food/item-form.html', context)

def update_item(request, pk):
    item = Item.objects.get(id=pk)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('home')

    context = {
        'form': form,
        'item': item,
    }

    return render(request, 'food/item-form.html', context)

def delete_item(request, pk):
    item = Item.objects.get(id=pk)
    context = {'item': item}

    if request.method == 'POST':
        item.delete()
        return redirect('home')

    return render(request, 'food/item-delete.html', context)