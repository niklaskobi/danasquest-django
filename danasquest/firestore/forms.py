from django import forms


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50, required=False)
    project_settings = forms.FileField()
    pic_cover = forms.FileField(required=False)
    pic_characters = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)
    pic_backgrounds = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)


