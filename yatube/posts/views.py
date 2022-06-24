from django.shortcuts import render

# Create your views here.
#from django.http import HttpResponse


# Главная страница
def group_posts(request):
    # Адрес шаблона сохраним в переменную, это не обязательно, но удобно
    template = 'posts/index.html'
    # Строку, которую надо вывести на страницу, тоже сохраним в переменную
    title = 'Yatube'
    # Словарь с данными принято называть context
    context = {
        # В словарь можно передать переменную
        'title': title,
        # А можно сразу записать значение в словарь. Но обычно так не делают
        'text': 'Группы проекта Yatube' ,
    }
    # Третьим параметром передаём словарь context
    return render(request, template, context)