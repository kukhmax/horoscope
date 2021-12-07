from django.urls import path
from . import views

urlpatterns = [
    path('<int:day_of_week>/', views.get_info_to_do_of_number_day),
    path('<str:day_of_week>/', views.get_info_to_do)
]