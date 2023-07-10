from danasquest.arcweave.models import AssetFile


def get_board_by_name(data, name):
    return next((board_data for board_data in data["boards"].values() if board_data.get("name") == name), None)


def get_board_by_id(data, id):
    return data["boards"][id]


def get_starting_element(data):
    id = data.get("startingElement")
    return get_element_by_id(data, id)


def get_element_by_id(data, id):
    """
    This function retrieves an element from a provided data structure by its ID, first attempting to access it directly
    from the 'elements' section, then if unsuccessful, by using a jumper's 'elementId' found in the 'jumpers' section.
    """
    element = data["elements"].get(id)
    if element is not None:
        return data["elements"][id]
    else:
        jumper = data["jumpers"].get(id)
        return get_element_by_id(data, jumper['elementId'])


def get_cover_asset_from_element(element, project):
    try:
        id = element["assets"]["cover"]["id"]
        return get_asset_by_id(project, id)
    except KeyError:
        return None


def get_image_assets_from_element(element, project):
    image_assets = []
    for component_id in element['components']:
        component = get_component_by_id(project, component_id)
        asset_id = component['assets']['cover']['id']
        image_assets.append(get_asset_by_id(project, asset_id))
    return image_assets


def get_component_by_id(project, component_id):
    return project.json['components'][component_id]


def get_asset_by_id(project, id):
    asset_name = project.json["assets"][id]["name"]
    return AssetFile.objects.get(project=project, name=asset_name)


def get_audio_assets_from_element(element, project):
    audio_assets = []
    try:
        for audio in element["assets"]["audio"]:
            audio_assets.append(get_asset_by_id(project, audio['asset']))
        return audio_assets
    except KeyError:
        return None


def get_connections_from_element(element, project):
    connections = []
    for id in element["outputs"]:
        next_element = project.json.get("connections").get(id)
        connections.append({"label": next_element.get("label"),
                            "target_id": next_element["targetid"]})
    return connections


def have_different_assets(element_old, element_new):
    try:
        # check covers
        if element_old["assets"]["cover"]["id"] != element_new["assets"]["cover"]["id"]:
            # check assets
            # we don't check audio assets, because they are handled separately
            if sorted(element_old["components"]) != sorted(element_new["components"]):
                return True
    except KeyError:
        return True
    return False
