from django import forms

class ImageForm(forms.Form):
    imagefile = forms.ImageField(label='Select and Image to Upload')