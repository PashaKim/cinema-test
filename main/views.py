from django.shortcuts import render, redirect
from .models import Menu, Film, News


def base_context(request):
    context = dict()
    context['domain'] = request.build_absolute_uri('/')[:-1]
    context['menus'] = Menu.objects.prefetch_related('menu_elements').all()
    return context


def main(request):
    context = base_context(request)
    context['selected_menu'] = '/'
    context['films'] = Film.objects.all()
    return render(request, 'content/main.html', context)


def films(request):
    context = base_context(request)
    context['selected_menu'] = '/films'
    context['films'] = Film.objects.all()
    return render(request, 'content/films.html', context)


def film(request, film_id=None):
    if not film_id:
        return redirect('films')
    context = base_context(request)
    context['selected_menu'] = '/films'
    context['film'] = Film.objects.get(id=film_id)
    return render(request, 'content/selected_item/film.html', context)


def news(request):
    context = base_context(request)
    context['selected_menu'] = '/news'
    context['news'] = News.objects.all()
    return render(request, 'content/news.html', context)
