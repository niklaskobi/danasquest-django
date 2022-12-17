from django import forms


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50, required=False)
    project_settings = forms.FileField()
    cover_pic = forms.FileField()
    pic_characters = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    pic_backgrounds = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))


