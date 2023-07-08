from danasquest.arcweave.models import AssetFile


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
        connections.append({"label": next_element.get("label"),
                            "target_id": next_element["targetid"]})
    return connections


def has_other_assets(element_old, element_new):
    # check covers
    if element_old["assets"]["cover"]["id"] != element_new["assets"]["cover"]["id"]:
        return True
    # check assets
    if sorted(element_old["components"]) != sorted(element_new["components"]):
        return True
    # we don't check audio assets, because they are handled separately
    return False
