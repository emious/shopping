from django import forms
from account.models import ProfileModel


class ProfileRegisterForm(forms.ModelForm):
    f_name = forms.CharField(max_length=100)
    l_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField(widget=forms.EmailInput)

    class Meta:
        model = ProfileModel
        fields = ['mobile']
