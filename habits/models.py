from django.db import models
from .models import Habit

# Create your models here.
class Habit(models.Model):
    habit_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    user_id = models.IntegerField()
    activity_value_type = models.CharField(max_length=10)  # 'int' lub 'float'

    def __str__(self):
        return self.name

class HabitActivity(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    activity_date = models.DateField()

    def happenedInPeriod(self, period_start, period_end):
        return period_start <= self.activity_date < period_end