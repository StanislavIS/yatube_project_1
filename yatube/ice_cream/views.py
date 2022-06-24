from django.shortcuts import render

# Create your views here.
# ice_cream/views.py
from django.http import HttpResponse
# Импортируем загрузчик.


# Главная страница
def index(request):
    # Адрес шаблона сохраним в переменную, это не обязательно, но удобно
    template = 'ice_cream/index.html'
    # Строку, которую надо вывести на страницу, тоже сохраним в переменную
    title = 'Yatube'
    # Словарь с данными принято называть context
    context = {
        # В словарь можно передать переменную
        'title': title,
        # А можно сразу записать значение в словарь. Но обычно так не делают
        'text': 'Главная страница',
    }
    # Третьим параметром передаём словарь context
    return render(request, template, context)
# Страница со списком мороженого
def ice_cream_list(request):
     # Адрес шаблона сохраним в переменную, это не обязательно, но удобно
    template = 'ice_cream/ice_cream_list.html'
    # Строку, которую надо вывести на страницу, тоже сохраним в переменную
    title = 'Yatube'
    # Словарь с данными принято называть context
    context = {
        # В словарь можно передать переменную
        'title': title,
        # А можно сразу записать значение в словарь. Но обычно так не делают
        'text': 'Список мороженого',
    }
    # Третьим параметром передаём словарь context
    return render(request, template, context)
    


# Страница с информацией об одном сорте мороженого;pyton manage.py runserver
# view-функция принимает параметр pk из path()
def ice_cream_detail(request, pk):
    template = 'ice_cream/ice_cream_detail.html'
    # Строку, которую надо вывести на страницу, тоже сохраним в переменную
    title = 'Yatube'
    # Словарь с данными принято называть context
    context = {
        # В словарь можно передать переменную
        'title': title,
        # А можно сразу записать значение в словарь. Но обычно так не делают
        'text': 'Список мороженого',
    }
    # Третьим параметром передаём словарь context
    return render(request, template, context)



