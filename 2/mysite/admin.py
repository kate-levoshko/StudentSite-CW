from django.contrib import admin

from mysite.models import Helper

class HelperAdmin(admin.ModelAdmin):
    fields = ['faculty_name', 'teacher', 'discipline_name', 'discipline_year', 'upload_material']

admin.site.register(Helper, HelperAdmin)
