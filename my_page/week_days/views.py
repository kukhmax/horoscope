from django.http import HttpResponse, HttpResponseNotFound

days_of_week = {
    'monday': '1.Пойти на работу<br>2.Зайти в магазин<br>3.Прийти с работы',
    'tuesday': '1.Выйти из дома<br>2.Войти в дом'
}


def get_info_to_do(request, day_of_week: str):
    todo = days_of_week.get(day_of_week)
    if todo:
        return HttpResponse(todo)


def get_info_to_do_of_number_day(request, day_of_week: int):
    if 1 <= day_of_week <= 7:
        return HttpResponse(f'Сегодня {day_of_week} день недели')
    else:
        return HttpResponse(f'Неверный номер дня - {day_of_week}')