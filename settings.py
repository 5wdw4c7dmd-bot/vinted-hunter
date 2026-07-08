import json


def load_settings():

    with open("settings.json", "r", encoding="utf-8") as f:

        return json.load(f)