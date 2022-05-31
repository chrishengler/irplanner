from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.template import loader

from .models import Series, Week


def index(request):
    series_list = Series.objects.order_by('series_name')
    template = loader.get_template('planner/index.html')
    context = {
        'series_list': series_list,
    }
    return render(request, 'planner/index.html', context)


def series(request, series_id):
    s = get_object_or_404(Series, pk=series_id)
    week_list = s.week_set.all()
    context = {
        'week_list': week_list
    }
    return render(request, 'planner/series.html', context)


def week(request, week_id):
    w = get_object_or_404(Week, pk=week_id)
    session_list = w.session_set.all()
    context = {
        'session_list': session_list
    }
    return render(request, 'planner/week.html', context)
