from django.db.models import fields
from django.db.models.fields import Field
from django.forms import ModelForm
from .models import TodoList
#create here:
class TodoListForm(ModelForm) : 
    class Meta:
        model = TodoList
        fields = '__all__'