from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('clean-empty-todo-items/', views.clean_empty_todo_items, name='clean_empty_todo_items'),
]

htmxpatterns = [
    path('add-task/', views.add_task, name='add_task'),
    path('update-task/<int:pk>/', views.update_task, name='update_task'),
    path('delete-task/<int:pk>/', views.delete_task, name='delete_task'),
]

urlpatterns += htmxpatterns