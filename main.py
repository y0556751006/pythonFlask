import json
from flask import Flask, request

with open('data.json', 'r') as f:
    data = json.load(f)
    app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# GET
@app.route("/capsules/byName/<name>")
def getName(name):
    for d in data:
        if d['name']==name:
            return d
    return "This name is not exist"
@app.route("/capsules/all")
def getAll():
    return data
@app.route("/capsules/byId/<id>")
def getId(id):
    for d in data:
        if d['id']==id:
            return d
    return "This id is not exist"
@app.route("/image/<id>")
def getImageId(id):
    for d in data:
        if d['image']==id:
            return d
    return "This id is not exist"
# POST
@app.route("/capsules/filterByProfile",methods=['POST'])
def byProfile():
   profile=request.json['profile']
   answer=[]
   for d in data:
     if sameProfile(d['profile'],profile)==True:
       answer.append(d)
   return str(answer)

def sameProfile(capsul,profile):
  for p in profile:
    if capsul[p]!=profile[p]:
      return False
  return True
# PUT
@app.route("/capsules/id",methods=['PUT'])
def putById():
    id=request.json
    for d in data:
        if d['id']==id:
            d['price']+=10
            with open('data.json', 'w') as jsonFile:
                json.dump( data, jsonFile)
    return id

if __name__ == '__main__':
    app.run()
