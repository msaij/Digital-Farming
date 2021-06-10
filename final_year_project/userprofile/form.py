from django import forms

class profilepicupload(forms.Form):
    file = forms.FileField()