from django import forms
from django.forms import ModelForm

from danasquest.firestore.models import Arcweave


class UploadFileForm(ModelForm):
    # title = forms.CharField(max_length=50, required=False)
    # project_settings = forms.FileField(required=False)
    # pic_cover = forms.ImageField(required=False)
    # pic_characters = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)
    # pic_backgrounds = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = Arcweave
        fields = '__all__'
        exclude = ()
        widgets = {}


