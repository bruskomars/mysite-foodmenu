from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
from django.template import loader
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# Create your views here.
def home(request):
    item = Item.objects.all()
    context = {
        'item': item,
    }
    return render(request, 'food/index.html', context)

class IndexClassView(ListView): # CLASS BASE VIEW - LIST VIEW
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'item'

def item(request):
    return HttpResponse("This is an Item View")

def detail(request, pk):
    item = Item.objects.get(pk=pk)
    context = {
        'item': item
    }
    return render(request, 'food/detail.html', context)

class FoodDetail(DetailView): # CLASS BASE VIEW - DETAIL VIEW
    model = Item
    template_name = 'food/detail.html'


def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('home')

    context={
        'form': form,
    }

    return render(request, 'food/item-form.html', context)

#CLASS BASED VIEW - CREATE VIEW
#CLASS BASED VIEW - CREATE VIEW
#CLASS BASED VIEW - CREATE VIEW
class CreateItem(CreateView):
    model = Item
    fields = ['item_name', 'item_desc', 'item_price', 'item_image']
    template_name = 'food/item-form.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user

        return super().form_valid(form)


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