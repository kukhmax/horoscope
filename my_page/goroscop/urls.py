from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:znak_zodiaka>/', views.get_info_about_sign_zodiac_by_number),
    path('<str:znak_zodiaka>/', views.get_info_about_sign_zodiac, name='goroscop-name'),
]
