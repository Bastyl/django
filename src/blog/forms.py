from django import forms

class AccountForm(forms.Form):
	username = forms.CharField(max_length=200)
	password = forms.CharField(max_length=200)
	email	 = forms.EmailField(max_length=200)
m
