import json

class TI:
    def input():
        f = open ('data.json', "r")
        data = json.loads(f.read())
        data = data["data"]
        f.close()
        return data