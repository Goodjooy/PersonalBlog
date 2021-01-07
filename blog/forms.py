from blog.models import Artical, Image
from django import forms
from django.forms.widgets import PasswordInput


class LoginForm(forms.Form):
    userName = forms.CharField(label="uid", max_length=100, empty_value="www")
    passWord = forms.CharField(label="密码", widget=forms.PasswordInput)


class ImageForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


class ArticalForm(forms.ModelForm):

    class Meta:
        model = Artical
        fields = ("title", "postData", "readCount", "text")

class ImageForm(forms.ModelForm):
    
    class Meta:
        model = Image
        fields = ("date","src")
