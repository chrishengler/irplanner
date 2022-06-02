from datetime import datetime, time
from django.db import models


class Series(models.Model):
    series_name = models.CharField(max_length=200)
    start_time = models.TimeField()
    time_between_sessions = models.DurationField()

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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        timeslots = list[time]()
        start_time = self.series.start_time
        timeslots.append(start_time)
        slot_datetime = datetime(2000, 1, 1, hour=start_time.hour, minute=start_time.minute)
        slot_datetime += self.series.time_between_sessions
        while slot_datetime < datetime(2000, 1, 2):
            timeslots.append(slot_datetime.time())
            slot_datetime += self.series.time_between_sessions
        Session.objects.filter(week=self).delete()
        for day in range(0, 7):
            for slot in timeslots:
                Session.objects.create(week=self, day=day, time=slot)


class Session(models.Model):
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    day = models.IntegerField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.week.__str__()}: day {self.day} at {self.time}"

    def day_name(self):
        return {0: "Tuesday",
                1: "Wednesday",
                2: "Thursday",
                3: "Friday",
                4: "Saturday",
                5: "Sunday",
                6: "Monday"}[self.day]


class Racer(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    car_class = models.ForeignKey(CarClass, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}: {self.session.__str__()}"
