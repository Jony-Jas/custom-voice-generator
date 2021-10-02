f = open ('data.json', "r")
data = json.loads(f.read())
for i in data['table']:
    print(i)
f.close()