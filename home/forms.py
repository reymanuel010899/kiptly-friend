from django.forms import ModelForm
from django import forms
from users.models import User
from django.forms import ClearableFileInput
class  userupdateavatar(ModelForm):
    avatar = forms.FileField(widget=ClearableFileInput(attrs={'Currently':False}))
    class Meta:
        model=User
        fields = ('avatar',)
       