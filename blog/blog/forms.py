from django import forms

class userCreationForm(forms.Form):
    username = forms.CharField(label="username", max_length=100)
    firstname = forms.CharField(label="first_name", max_length=100)
    lastname = forms.CharField(label="last_name", max_length=100)
    password = forms.CharField(label="password", max_length=100)