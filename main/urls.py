from django.urls import path
from .views import *
from .models import *
app_names='mainapp'

urlpatterns = [
    path('',TodoListView.as_view(), name='home'),
    path('create/',CreateListView.as_view(),name='create'),
    path('<pk>/', DetailToDo.as_view(), name='detail'),
    path('<pk>/update', UpdateTodo.as_view(), name='update'),
    path('<pk>/delete', DeleteToDO.as_view(), name='delete'),
]