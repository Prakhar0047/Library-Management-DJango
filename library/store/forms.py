from django import forms
from store.models import lib_user_model, book
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class new_lib_user_form(forms.ModelForm):

    class Meta():
        model = lib_user_model
        fields = '__all__'

class new_lib_book_form(forms.ModelForm):

    class Meta():
        model = book
        fields = '__all__'