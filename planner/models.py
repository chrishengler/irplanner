from django.db import models


class Series(models.Model):
    series_name = models.CharField(max_length=200)


class CarClass(models.Model):
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    class_name = models.CharField(max_length=200)


class Week(models.Model):
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    track = models.CharField


class Session(models.Model):
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    time = models.TimeField()


class Racer(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    car_class = models.ForeignKey(CarClass, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
