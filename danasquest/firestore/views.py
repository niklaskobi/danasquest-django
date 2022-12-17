from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import UploadFileForm


# Create your views here.
def firestore_upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_settings_file(request.FILES['project_settings'])
            payload = {
                "message": "Export to firestore was successful",
                "button_link":
                    {
                        "link": reverse('home'),
                        "label": "ok, nice, now go back"
                    }
            }

            return render(request, 'arcweave/export_succesfull.html', payload)
    else:
        form = UploadFileForm()
    return render(request, 'arcweave/export_to_firestore.html', {'form': form})


def handle_uploaded_settings_file(f):
    # with open('some/file/name.txt', 'wb+') as destination:
    print(f"Handling uploaded file: {f.name}")
    for chunk in f.chunks():
        # destination.write(chunk)
        print(chunk)
