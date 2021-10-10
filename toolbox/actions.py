import json
import os


class Actions():
    def audio():
        f = open('data.json', "r")
        data = json.loads(f.read())
        data = data["sample"]
        f.close()
        path = data
        return path

    def input():
        f = open('data.json', "r")
        data = json.loads(f.read())
        data = data["data"]
        f.close()
        return data

    def save():
        f = open('data.json', "r")
        data = json.loads(f.read())
        id = data["id"]
        f.close()
        directory = os.path.join(os.getcwd(), "../cloned_audios")
        fpath = os.path.abspath(directory) +"/"+id
        return fpath
