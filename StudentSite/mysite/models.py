from django.db import models
from django.contrib.auth.models import User

class Help_materials(models.Model):
    class Meta:
        db_table = "hmaterials"

    faculty = models.CharField(max_length=50)
    professor = models.CharField(max_length=50)
    discipline = models.CharField(max_length=50)
    year_discipline = models.IntegerField()
    upload_material = models.FileField(upload_to='downloads/')
    description = models.TextField(default='')
    users = models.ManyToManyField(User, related_name='my_material')

    def dict(self):
        return {'id': self.id,
                'faculty': self.faculty,
                'professor': self.professor,
                'discipline': self.discipline,
                'year_discipline': self.year_discipline,
                'upload_material': self.upload_material.url,
                'description': self.description,
                'users': [{'id': i.id, 'username': i.username} for i in self.users.all()]}

