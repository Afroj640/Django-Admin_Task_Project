from django.urls import path
from . import views

app_name = 'taskapp'

urlpatterns = [
    path('', views.user_page ,name='user_page'),
    path('login/', views.login_pages, name='login_pages'),
    path('Task/', views.task_page, name='task_page'),
]