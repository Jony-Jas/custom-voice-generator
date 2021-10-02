import json

class Actions():
    def audio():
        f = open ('data.json', "r")
        data = json.loads(f.read())
        data = data["sample"]
        f.close()
        path = data
        return path
    def input():
        f = open ('data.json', "r")
        data = json.loads(f.read())
        data = data["data"]
        f.close()
        return data
    def save():
        f = open ('data.json', "r")
        data = json.loads(f.read())
        id = data["id"]
        f.close()
        fpath = "C:/Users/jonyj/Documents/Project/Ongoing/Hackathon/Voice Cloning/cloned_audios/"+id
        return fpath