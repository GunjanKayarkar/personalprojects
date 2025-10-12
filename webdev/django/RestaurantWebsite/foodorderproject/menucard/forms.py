from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class OrderForm(ModelForm):
    class Meta:
        model = Orderid
        fields = '__all__'

class CreateForm(ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'

class UpdateForm(ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'

class DeleteForm(ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('email', 'password1')