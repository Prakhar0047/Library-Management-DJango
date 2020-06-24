from django import forms
from issuing.models import issuing
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class book_issuing(forms.ModelForm):
    
    class Meta():
        model = issuing
        fields = '__all__'