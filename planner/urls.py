from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('series/<int:series_id>/', views.series, name='series'),
    path('week/<int:week_id>/', views.week, name='week'),
]