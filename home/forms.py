from django.forms import ModelForm
from django import forms
from users.models import User
from django.forms import ClearableFileInput

class  userupdateavatar(ModelForm):
    avatar = forms.FileField(required=False)
    class Meta:
        model=User
        fields = ('avatar',)
       
    
    def __init__(self, *args, **kwars):
        super(userupdateavatar, self).__init__(*args, **kwargs)
        self.fields['avatar'].initial = None
        