from django import forms
from .models import Movie
from django.forms.widgets import NumberInput, DateInput

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields ='__all__'
        # fields = ('genre','score','release_date')
        widgets = {
            'score' : NumberInput(attrs={
                'min': 0,
                'max': 5.0,
                'step' : 0.5,
            }),
            'release_date': DateInput(attrs={
                'type' : 'date'
            }),
        }