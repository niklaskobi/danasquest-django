def _get_submit_index(dict):
    for key in dict:
        if key.startswith("submit_"):
            return key.split("_")[1]
    return None


def _get_target_id_by_index(dict, index):
    return dict.get(f"target_id_{index}")


def get_target_id(request_post):
    """
    From a given request.POST return the target_id taking into account the index from the submit key:
    If this is the request.POST:
    {'submit_1': ['BlaBla'],
        'csrfmiddlewaretoken': ['dmPV2t0H9JblylpdRekACF2WOD3kUjMCdDevEhj6HIJTOItIHgHrux0FTP5gyohP'],
        'target_id_0': ['53365156-743b-42de-bc75-7fbfeae20c11'],
        'target_id_1': ['123123'],
        'current_id': ['00ff3647-fc59-4fcf-9f83-be9043a4956d']}
    then the "1231232" is returned.
    index "1" is taken from the "submit_1" key and then "target_id_1" is returned
    """
    index = _get_submit_index(request_post)
    return _get_target_id_by_index(request_post, index)
