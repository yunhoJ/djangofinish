from django import forms
from .models import *
  
class ImgForm(forms.ImageField):
  
    class Meta:
        model = Images
        fields = ['Images']
