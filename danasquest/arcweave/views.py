from django.shortcuts import render

from danasquest.arcweave.models import ArcweaveProject
from danasquest.arcweave.parse import get_element_by_id, get_cover_asset_from_element, get_audio_assets_from_element, \
    get_connections_from_element, have_different_assets, get_image_assets_from_element


# DEBUG_STARTING_ELEMENT = '791c60c7-6cb2-40ba-8c79-4f629c2fc206'
DEBUG_STARTING_ELEMENT = '0e1fde1e-1914-496f-b99d-8332466d792c'

# Create your views here.
def view_import(request):
    project = ArcweaveProject.objects.filter().first()
    if DEBUG_STARTING_ELEMENT:
        element = get_element_by_id(project.json, DEBUG_STARTING_ELEMENT)
    else:
        element = get_element_by_id(project.json, project.json.get("startingElement"))
    payload = get_payload(project, element, project.json.get("startingElement"))

    # return render(request, 'arcweave/page.html', payload)
    return render(request, 'base.html', payload)


def get_payload(project, element, element_id):
    cover = get_cover_asset_from_element(element, project)
    audio_list = get_audio_assets_from_element(element, project)
    connections = get_connections_from_element(element, project)
    images = get_image_assets_from_element(element, project)
    char_left = next(iter(images[0:1]), None)
    char_right = next(iter(images[1:2]), None)
    payload = {
        'project_id': project.id,
        'content': element["content"],
        'connections': connections,
        'element_id': element_id,
        'assets': {
            'background': cover,
            'audio': audio_list,
            'char_left': char_left,
            'char_right': char_right,
        }
    }
    return payload


def next_element(request, project_id):
    if request.method == 'POST':
        #todo save project in the
        project = ArcweaveProject.objects.get(id=project_id)
        element = get_element_by_id(project.json, request.POST.get("target_id"))
        payload = get_payload(project, element, request.POST.get("target_id"))
        # new
        prev_element_id = request.POST.get("current_id")
        # todo: use postgres json commands instead of loading the whole json each time
        prev_element = get_element_by_id(project.json, prev_element_id)
        update_whole_scene = have_different_assets(prev_element, element)
        if update_whole_scene:
            return render(request, 'game/body.html', payload)
        else:
            return render(request, 'game/dialogue.html', payload)


def view_import_backup(request):
    payload = {
        'title': 'Import',
        'urls': {
            'background': '../static/arcweave/danas-quest-2023-05-17-130459/assets/Locations/Episode_1/kitchen.png',
            'char_left': '../static/arcweave/danas-quest-2023-05-17-130459/assets/Characters/original/Dana.png',
            'char_right': '../static/arcweave/danas-quest-2023-05-17-130459/assets/Characters/original/Marta.png',
        }
    }

    # return render(request, 'arcweave/page.html', payload)
    return render(request, 'base.html', payload)
