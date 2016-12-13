from django import forms

class upload_file_form(forms.Form):
    material = forms.FileField()
