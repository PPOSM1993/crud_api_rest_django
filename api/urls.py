from django.urls import path
from . import views


urlpatterns = [
    path('get/',  views.GetTasks),
    path('post/',  views.CreateTasks),
    path('put/<int:pk>/', views.PutTasks),
    path('delete/<int:pk>/', views.DeleteTasks),
]
