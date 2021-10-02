import json

class AudioSample:
    def audio():
        f = open ('data.json', "r")
        data = json.loads(f.read())
        data = data["sample"]
        f.close()
        path = data
        return path