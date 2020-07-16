from django.urls import path 
from . import views

app_name = 'calcs'


urlpatterns = [
   path('', views.home_page, name='home_page'),
   path('ohms-law/', views.ohms_law, name='ohms_law'),
   path('leave-message/', views.leave_message, name='leave_message')

]