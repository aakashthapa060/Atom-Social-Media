from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from django.forms.widgets import PasswordInput
User = get_user_model()

unallowed_username = ['fuck', 'fuck123', 'bitch', 'yourdad', 'yourmom','suck']

class LoginForm(forms.ModelForm):
    username= forms.CharField()
    password = forms.CharField(
        widget=PasswordInput(
            attrs={
                "class": "login-password form-control",
                "id": "login-password"
            }
        )
    )

    def clean_username(self):
        username = self.cleaned_data["username"]
        qs = User.objects.filter(username__iexact = username)
        if qs == None:
            raise forms.ValidationError("Username Not Found, Please pick valid Username")
        return username

class RegisterForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    username = forms.CharField()
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(

            attrs = {
                "class": "form-control user-password1",
                "id": "user-password"
            }
        )
    )
    
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(
            attrs = {
                "class": "form-control user-password2",
                "id": "user-confirm-password"
            }
        )
    )
    class Meta:
        model = User
        fields = ["first_name", "last_name","username", "email", "password1","password2"]

    
    def clean_username(self):
        username = self.cleaned_data["username"]
        qs = User.objects.filter(username__iexact = username)
        if username in unallowed_username:

            raise forms.ValidationError("This username is restricted, Please pick another")
        if qs.exists():
            print("invalid username")
            raise forms.ValidationError(("This is an Invalid Username, Please pick another"))
    
        
        return username

    def clean_email(self):
        email = self.cleaned_data["email"]
        qs = User.objects.filter(email__iexact = email)
        if qs.exists():
            raise forms.ValidationError("This email is already in use.")
        return email

    def clean_password(self):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]
        if password1 != password2:
            raise forms.ValidationError("Password 1 and Password 2 Don't match")
        
        return password1


