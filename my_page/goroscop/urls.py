from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, 'yyyy')
register_converter(converters.MyFloatConverter, 'my_float')
register_converter(converters.MyDateConverter, 'my_date')

urlpatterns = [
    path('', views.index, name='goroscop-index'),
    path('type/', views.get_types),
    path('type/<element>/', views.get_elements, name='type-name'),
    path('<my_date:znak_zodiaka>/', views.get_my_date_converters),
    path('<yyyy:znak_zodiaka>/', views.get_yyyy_converters),
    path('<int:znak_zodiaka>/', views.get_info_about_sign_zodiac_by_number),
    path('<my_float:znak_zodiaka>/', views.get_my_float_converters),
    path('<str:znak_zodiaka>/', views.get_info_about_sign_zodiac, name='goroscop-name'),
]
