from django import forms
from .models import *  

class YourForm(forms.ModelForm):
    class Meta:
        model = MeetingSphere 
        fields = ['code', 'date', 'message', 'cat', 'cuisine', 'place' ]



       