
from djongo import models

class Team(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=50)
    def __str__(self):
        return self.email


class Activity(models.Model):
    user = models.EmbeddedField(model_container=User)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    date = models.DateField()


class Leaderboard(models.Model):
    team = models.EmbeddedField(model_container=Team)
    points = models.IntegerField()

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    difficulty = models.CharField(max_length=50)
