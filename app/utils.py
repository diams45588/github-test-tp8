import json

def format_result(operation, result):
    return {'operation': operation, 'result': result}

def save_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

def load_from_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)
