import json

class SaveFile:
    def save():
        f = open ('data.json', "r")
        data = json.loads(f.read())
        id = data["id"]
        f.close()
        fpath = "C:/Users/jonyj/Documents/Project/Ongoing/Hackathon/Voice Cloning/cloned_audios/"+id
        return fpath