# ice_cream/urls.py
from django.urls import path
from . import views

# anfisa/ice_cream/urls.py
# Эта строчка обязательна. 
# Без неё namespace работать не будет:
# namespace должен быть объявлен при include и тут, в app_name
app_name = 'ice_cream'

urlpatterns = [
    # Главная страница
    path('', views.index),
    # Страница со списком сортов мороженого
    path('ice_cream_list/', views.ice_cream_list, name='ice_cream_list'),
    # Отдельная страница с информацией о сорте мороженого
    path('ice_cream_detail/<int:pk>/', views.ice_cream_detail, name='ice_cream_detail'),
]