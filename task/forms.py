from dataclasses import field
from django import forms
from django.contrib.auth.models import User
from task.models import Task

class RegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["first_name","last_name","username","password"]
        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control border border-dark bg-light"}),
            "last_name":forms.TextInput(attrs={"class":"form-control border border-dark bg-light"}),
            "username":forms.TextInput(attrs={"class":"form-control border border-dark bg-light"}),
            "password":forms.PasswordInput(attrs={"class":"form-control border border-dark bg-light"}),
        }
    
class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-dark bg-light","placeholder":"your username"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control border border-dark bg-light","placeholder":"password Here"}))

class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=["task_name","status"]

