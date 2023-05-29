from django.shortcuts import render


# Create your views here.
def view_import(request):
    payload = {
        'title': 'Import',
        'urls': {
            'background': '../../static/arcweave/danas-quest-2023-05-17-130459/assets/Locations/Episode_1/kitchen.png',
            'char_left': '../../static/arcweave/danas-quest-2023-05-17-130459/assets/Characters/original/Dana.png',
            'char_right': '../../static/arcweave/danas-quest-2023-05-17-130459/assets/Characters/original/Marta.png',
        }
    }

    return render(request, 'arcweave/page.html', payload)
