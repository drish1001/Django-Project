from django import forms
from django.contrib.auth.models import User
from . import models

class MovieForm(forms.ModelForm):
	class Meta():
		model = model.movielist
		field = {'name','about' , 'date','image'}