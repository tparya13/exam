from .models import Task
from django import forms 


class TodoForm(forms.ModelForm):
    class Meta:
        model =Task
        fields =['task','priority','date','image']
    