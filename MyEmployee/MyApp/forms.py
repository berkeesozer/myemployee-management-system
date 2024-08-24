from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'job_title', 'birth_date', 'start_date', 'home_address', 'mailing_address','photo']

   
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label='username')
    password = forms.CharField(widget=forms.PasswordInput, label='password') 