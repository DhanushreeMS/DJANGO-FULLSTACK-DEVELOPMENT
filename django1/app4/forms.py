from django import forms

class WordInputForm(forms.Form):
    word = forms.CharField(label='Enter a 3, 4, or 5-letter word:', max_length=5)
