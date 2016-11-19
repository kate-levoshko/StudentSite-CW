from django.contrib import admin

from mysite.models import Help_materials

class MaterialsAdmin(admin.ModelAdmin):
    fields = ['faculty', 'professor', 'discipline', 'year_discipline', 'upload_material']

admin.site.register(Help_materials, MaterialsAdmin)
