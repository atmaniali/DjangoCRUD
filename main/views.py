from django.shortcuts import (redirect, render, get_object_or_404,HttpResponseRedirect)
from django.views import generic
from .forms import *
from .models import *

# Create your views here.
def home(request):
    template= "home.html"
    form = TodoListForm()
    context = {}
    if request.method == 'POST':
        form = TodoListForm(request.POST or None)
        if form.is_valid():
            form.save()
    context['form'] = form        
    return render(request,template,context)
def detait(request, id):
    template_name = ''
    context = {}
    context['data'] = TodoList.objects.get(id = id)
    return render(request,template_name,context)
def update(request, id):
    template_name = ''
    context = {}  
    obj = get_object_or_404(TodoList,id= id)
    form = TodoListForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        # return to detail 
        return HttpResponseRedirect("/"+id)
    context['form'] = form
    return  render(request,template_name,context)  
        
class TodoListView(generic.list.ListView):
    model = TodoList
    template_name = 'home.html'   
class CreateListView(generic.edit.CreateView):
    model = TodoList
    fields = ['title', 'text']
    template_name = 'create.html'
    def form_valid(self, form):
        return redirect('home')
class DetailToDo(generic.detail.DetailView):
    model = TodoList   
    template_name = 'detail.htm'  
class UpdateTodo(generic.edit.UpdateView):
    template_name = 'update.html'   
    model = TodoList   
    fields = ['title', 'text']  
    success_url ="/"
class DeleteToDO(generic.edit.DeleteView):
    template_name = 'delete.html'  
    model = TodoList 
    success_url ="/"  