from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.template import loader

from .models import Series, Session, Week


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
    session_list = w.session_set.all().order_by('time')
    session_matrix = list[list[Session]]()
    for day in range(0, 7):
        session_matrix.append(list[Session]())
    for session in session_list:
        session_matrix[session.day].append(session)
    context = {
        'session_matrix': session_matrix
    }
    return render(request, 'planner/week.html', context)
