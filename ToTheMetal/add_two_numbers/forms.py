from django import forms

class AddTwoNumbersForm(forms.Form):
    """A form for adding two numbers together"""
    number1 = forms.IntegerField(label="number1")
    number2 = forms.IntegerField(label="number2")
