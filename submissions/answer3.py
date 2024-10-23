from typing import Dict, Any

def flatten_dict(nested_dict: Dict[str, Any], sep: str = '.') -> Dict[str, Any]:
    """
    Flattens a nested dictionary into a single-level dictionary with dot notation for keys.
    
    :param nested_dict: The dictionary object to flatten.
    :param sep: The separator to use between parent and child keys (defaults to '.').
    :return: A flattened dictionary.
    """
    flat_dict = {}

    def flatten(current_key: str, value: Any):
        # If value is a dictionary, recursively flatten it
        if isinstance(value, dict):
            for k, v in value.items():
                new_key = f"{current_key}{sep}{k}" if current_key else k
                flatten(new_key, v)
        # If value is a list, iterate through it and flatten
        elif isinstance(value, list):
            for i, item in enumerate(value):
                new_key = f"{current_key}[{i}]"
                flatten(new_key, item)
        # If the value is neither a dict nor a list, just assign it
        else:
            flat_dict[current_key] = value

    # Initialize the flattening process
    flatten('', nested_dict)

    return flat_dict


nested_dict = {
    "road": {
        "name": "Highway 1",
        "length": 350,
        "sections": [
            {
                "id": 1,
                "condition": {
                    "pavement": "good",
                    "traffic": "moderate"
                }
            }
        ]
    }
}

flattened = flatten_dict(nested_dict)
print(flattened)
