from django import forms


class RegisterForm(forms.Form):
    first_name = forms.CharField(label="First name", max_length=100, required=True)
    last_name = forms.CharField(label="First mame", max_length=100, required=True)
    email = forms.CharField(label="Email", max_length=100, required=True)
    username = forms.CharField(label="Username", max_length=25, required=True)
    password = forms.CharField(label="password", required=True)
    family_name = forms.CharField(label="Family Name", required=True)
