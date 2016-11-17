from django.db import models

class Helper (models.Model):
    class Meta:
        db_table = 'helper'

    faculty_name = models.CharField(max_length=50, default='DEFAULT VALUE')
    teacher = models.CharField(max_length=50, default='DEFAULT VALUE')
    discipline_name = models.CharField(max_length=50, default='DEFAULT VALUE')
    discipline_year = models.IntegerField(default=0)
    up_material = models.FileField(default=0)