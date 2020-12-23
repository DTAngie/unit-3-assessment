from django.shortcuts import render
from .models import Item
from django.views.generic.edit import CreateView
from .forms import ItemForm

# Create your views here.
def index(request):
    items = Item.objects.all()
    return render(request, 'index.html', {'items': items})

class ItemCreate(CreateView):
    model = Item
    fields = ['description']
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(ItemCreate, self).get_context_data(**kwargs)
        context['form'] = ItemForm()
        return context