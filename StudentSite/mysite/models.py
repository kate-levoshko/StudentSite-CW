from django.db import models

class Help_materials(models.Model):
    class Meta:
        db_table = "hmaterials"

    faculty = models.CharField(max_length=50)
    professor = models.CharField(max_length=50)
    discipline = models.CharField(max_length=50)
    year_discipline = models.IntegerField()
    upload_material = models.FileField(upload_to='downloads/')

    def dict(self):
        return {'id':self.id,
                'faculty': self.faculty,
                'professor': self.professor,
                'discipline': self.discipline,
                'year_discipline': self.year_discipline,
                'upload_material': self.upload_material.url}