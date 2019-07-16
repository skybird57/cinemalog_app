from django import forms

class PushForm(forms.Form):
    token_name=forms.CharField(initial="Enter your token string: ", max_length=250)
    message=forms.CharField(initial="Enter your message")
    title=forms.CharField(initial="Enter ypur title message")
