from django.shortcuts import render

from danasquest.arcweave.models import ArcweaveProject, AssetFile


def get_board_by_name(data, name):
    return next((board_data for board_data in data["boards"].values() if board_data.get("name") == name), None)


def get_board_by_id(data, id):
    return data["boards"][id]


def get_starting_element(data):
    id = data.get("startingElement")
    return get_element_by_id(data, id)


def get_element_by_id(data, id):
    return data["elements"][id]


def get_cover_asset_from_element(element, project):
    id = element["assets"]["cover"]["id"]
    return get_asset_by_id(project, id)


def get_asset_by_id(project, id):
    asset_name = project.json["assets"][id]["name"]
    return AssetFile.objects.get(project=project, name=asset_name)


def get_audio_assets_from_element(element, project):
    audio_assets = []
    if element.get("assets").get("audio") is not None:
        for audio in element["assets"]["audio"]:
            audio_assets.append(get_asset_by_id(project, audio['asset']))
    return audio_assets


def get_connections_from_element(element, project):
    connections = []
    for id in element["outputs"]:
        next_element = project.json.get("connections").get(id)
        connections.append({"label": next_element.get("label"), "target_id": next_element["targetid"]})
    return connections

# Create your views here.
def view_import(request):
    project = ArcweaveProject.objects.filter().first()
    payload = get_payload(project, project.json.get("startingElement"))

    # return render(request, 'arcweave/page.html', payload)
    return render(request, 'base.html', payload)


def get_payload(project, element_id):
    element = project.json["elements"][element_id]
    cover = get_cover_asset_from_element(element, project)
    audio_list = get_audio_assets_from_element(element, project)
    connections = get_connections_from_element(element, project)
    payload = {
        'project_id': project.id,
        'title': 'Import',
        'content': element["content"],
        'connections': connections,
        'assets': {
            'background': cover,
            'audio': audio_list,
            'char_left': '../static/arcweave/danas-quest-2023-05-17-130459/assets/Characters/original/Dana.png',
            'char_right': '../static/arcweave/danas-quest-2023-05-17-130459/assets/Characters/original/Marta.png',
        }
    }
    return payload


def next_element(request, project_id):

    if request.method == 'POST':
        project = ArcweaveProject.objects.get(id=project_id)
        payload = get_payload(project, request.POST.get("target_id"))
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
