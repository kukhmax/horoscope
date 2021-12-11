from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from dataclasses import dataclass
#from django.template.loader import render_to_string

zodiac_dict = {
    "aries": "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля)",
    "taurus": "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая)",
    "gemini": "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня)",
    "cancer": "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля)",
    "leo": "Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа)",
    "virgo": "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября)",
    "libra": "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября)",
    "scorpio": "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября)",
    "sagittarius": "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря)",
    "capricorn": "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января",
    "aquarius": "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля)",
    "pisces": "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)",
}


types = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces'],
}

def get_yyyy_converters(request, znak_zodiaka):
    return HttpResponse(f'Вы передали число из четырех цыфр - {znak_zodiaka}')


def get_my_float_converters(request, znak_zodiaka):
    return HttpResponse(f'Вы передали вещественное число - {znak_zodiaka}')


def get_my_date_converters(request, znak_zodiaka):
    return HttpResponse(f'Вы передали дату: {znak_zodiaka}')


def index(request):
    zodiacs = list(zodiac_dict)
    # f"<li><a href='{redirect_path}'>{sign.title()}</a></li>"
    context = {
        'zodiacs': zodiacs,
        'zodiac_dict': zodiac_dict,
    }
    return render(request, 'goroscop/index.html', context=context)


def get_types(request):
    elements = list(types)
    li_types = ''
    for el in elements:
        redirect_path = reverse('type-name', args=[el])
        li_types += f"<li><a href='{redirect_path}'>{el.title()}</a></li>"
    response = f"""
    <ol>
        {li_types}
    </ol>
    """
    return HttpResponse(response)


def get_elements(request, element):
    list_of_sing_element = types[element]
    li_sings_of_element = ''
    for sing in list_of_sing_element:
        redirect_url = reverse('goroscop-name', args=[sing])
        li_sings_of_element += f"<li><a href='{redirect_url}'>{sing.title()}</a></li>"
    response = f"""
    <ol>
        {li_sings_of_element}
    </ol>
    """
    return HttpResponse(response)


@dataclass
class Person:
    name: str
    age: int


    def __str__(self) -> str:
        return f'This is {self.name}'
        



def get_info_about_sign_zodiac(request, znak_zodiaka: str):
    description = zodiac_dict.get(znak_zodiaka)
    data = {
        'description_zodiac': description,
        'sing': znak_zodiaka,
        'my_int': 5,
        'my_float': 7.7575,
        'my_list': [1, 2, 3],
        'my_tuple': (1, 2, 3, 4, 5),
        'my_dict': {'name': 'Jack', 'age': 40},
        'my_class': Person('Will', 55),
        'value': [],
        'value1': [9,0,0],
    }
    return render(request, 'goroscop/info_zodiac.html', context=data)


def get_info_about_sign_zodiac_by_number(request, znak_zodiaka: int):
    zodiac = list(zodiac_dict)
    if znak_zodiaka > len(zodiac):
        return HttpResponse(f'Неправильный порядковый номер зодиака - {znak_zodiaka}')
    name_zodiac = zodiac[znak_zodiaka - 1]
    redirect_url = reverse('goroscop-name', args=(name_zodiac, ))
    return HttpResponseRedirect(redirect_url)
