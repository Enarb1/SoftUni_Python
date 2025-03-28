from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView

from Frutipedia.fruitipediaApp.forms import CategoryAddForm, AddFruitForm, EditFruitForm, DeleteFruitForm
from Frutipedia.fruitipediaApp.models import Fruit


# Create your views here.

def index(request):
    return render(request, 'common/index.html')

def dashboard(request):
    fruits = Fruit.objects.all()
    context = {
        'fruits': fruits
    }
    return render(request, 'common/dashboard.html', context)

class CreateFruitView(CreateView):
    model = Fruit
    form_class = AddFruitForm
    template_name = 'fruits/create-fruit.html'
    success_url = reverse_lazy('dashboard')

def details_view(request, pk):
    fruit = Fruit.objects.get(pk=pk)

    context = {
        'fruit': fruit
    }
    return render(request, 'fruits/details-fruit.html', context)

def edit_view(request, pk):
    fruit = Fruit.objects.get(pk=pk)

    if request.method == 'GET':
        form =  EditFruitForm(instance=fruit)
    else:
        form = EditFruitForm(request.POST, instance=fruit)

        if form.is_valid():
            form.save()
            return redirect('dashboard')


    context = {
        'form': form,
        'fruit': fruit
    }

    return render(request, 'fruits/edit-fruit.html', context)


class DeleteFruitView(DeleteView):
    model = Fruit
    form_class = DeleteFruitForm
    template_name = 'fruits/delete-fruit.html'
    success_url = reverse_lazy('dashboard')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class(instance=self.object)
        return self.render_to_response(self.get_context_data(form=form, object=self.object))

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.get_success_url())


def delete_view(request, pk):
    return render(request, 'fruits/delete-fruit.html')

def create_category_view(request):

    if request.method == 'GET':
        form = CategoryAddForm()
    else:
        form = CategoryAddForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form
    }
    return render(request, 'categories/create-category.html', context)


