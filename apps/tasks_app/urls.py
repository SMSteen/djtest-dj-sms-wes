from django.urls import path, include
from . import views

urlpatterns = [
    path('tasks/', views.index),
    path('tasks/<int:task_id>', views.show),
    path('tasks/<int:task_id>/delete', views.destroy),
    path('people/', views.index_people),
]
