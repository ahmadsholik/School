from django.db import models


class Week(models.Model):
    owner = models.CharField(max_length=50)  # just a placeholder, should be user

    def __str__(self):
        return "Week object: owner={}".format(self.owner)


class Song(models.Model):
    file = models.FileField()
    title = models.CharField(max_length=50)
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    day = models.IntegerField(default=0)

    def __str__(self):
        return "{} - Song number {} of {}'s week".format(self.title, self.day, self.week.owner)
