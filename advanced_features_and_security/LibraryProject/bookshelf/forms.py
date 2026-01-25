from django import forms

class ExampleForm(forms.Form):
    """
    A simple form used to demonstrate secure data handling.
    Using Django forms ensures that input is cleaned and validated.
    """
    title = forms.CharField(max_length=100, required=True, label="Book Title")
    author = forms.CharField(max_length=50, required=True, label="Author")
    # You can add more fields as needed for your application