from django.db import models


class Series(models.Model):
    series_name = models.CharField(max_length=200)

    def __str__(self):
        return self.series_name


class CarClass(models.Model):
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    class_name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.series.series_name} ({self.class_name})"


class Week(models.Model):
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    week_no = models.IntegerField()
    track = models.CharField

    def __str__(self):
        return f"{self.series.series_name} week {self.week_no}"


class Session(models.Model):
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    time = models.TimeField()

    def __str__(self):
        return f"{self.week.__str__()} at {self.time}"


class Racer(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    car_class = models.ForeignKey(CarClass, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}: {self.session.__str__()}"
