import requests
response = requests.get("http://bluewater10000.pythonanywhere.com/api/fridgeFoods")

import json
def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())
