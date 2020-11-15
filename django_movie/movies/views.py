from django.shortcuts import render
from django.views.generic.base import View

from .models import Movie


class MoviesView(View): # создаю класс с аргументом view django
    ### Список фильмов
    def get(self, request): # функция get запросы инф. от нашего клиента
        movies = Movie.objects.all() # запрос передаем
        return render(request, "movies/movie_list.html", {"movie_list": movies})
        # return возвращаем ответ в виде нашего html страницы