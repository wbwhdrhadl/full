from fastapi import FastAPI
from pymongo import mongo_client
from bson.objectid import ObjectId
import pydantic
import os.path
import json

pydantic.json.ENCODERS_BY_TYPE[ObjectId] = str

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath("./")))
secret_file = os.path.join(BASE_DIR, '../../secret.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        errorMsg = "Set the {} environment variable.".format(setting)
        return errorMsg

HOSTNAME = get_secret("ATLAS_Hostname")
USERNAME = get_secret("ATLAS_Username")
PASSWORD = get_secret("ATLAS_Password")

client = mongo_client.MongoClient(f'mongodb+srv://{USERNAME}:{PASSWORD}@{HOSTNAME}')
print('Connected to Mongodb...')

mydb = client['test']
mycol = mydb['testdb']

@app.get('/')
async def healthcheck():
    return "OK"

from fastapi import FastAPI
from bson.objectid import ObjectId
from pymongo import mongo_client
import pydantic
import os.path
import json

pydantic.json.ENCODERS_BY_TYPE[ObjectId] = str

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath("./")))
secret_file = os.path.join(BASE_DIR, '../../secret.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        errorMsg = "Set the {} environment variable.".format(setting)
        return errorMsg

HOSTNAME = get_secret("ATLAS_Hostname")
USERNAME = get_secret("ATLAS_Username")
PASSWORD = get_secret("ATLAS_Password")

client = mongo_client.MongoClient(f'mongodb+srv://{USERNAME}:{PASSWORD}@{HOSTNAME}')
print('Connected to Mongodb...')

mydb = client['test']
mycol = mydb['testdb']

@app.get('/')
async def healthcheck():
    return "OK"

@app.get('/getmongo')
async def getMongo():
    data = list(mycol.find({}, {"_id":0}).limit(10))
    print(data)
    return data

@app.get('/getuser')
async def getUser(id=None):
    if id is None:
        return 'id를 입력하세요.'
    result = mycol.find_one({"id":id}, {"_id":0})
    if result:
        print(result)
        return result
    else:
        return '검색 결과가 없습니다.'

@app.get('/useradd')
async def userAdd(id=None, name=None):
    if (id and name) is None:
        return "id, name을 입력하세요."
    else:
        user = dict(id=id, name=name)
        mycol.insert_one(user)
        result = mycol.find_one({"id":id}, {"_id":0})
        print(result)
        return result
    
@app.get('/userupdate')
async def userUpdate(id=None, name=None):
    if (id and name) is None:
        return "id, name을 입력하세요."
    else:
        user = mycol.find_one({"id":id}, {"_id":0})
        if user:
            filter = {'id':id}
            data = {"$set":{'name':name}}
            mycol.update_one(filter, data)
            result = mycol.find_one({"id":id}, {"_id":0})
            print(result)
            return result
        else:
            return f'id = {id} 데이터가 존재하지 않습니다.'

@app.get('/userdelete')
async def userDelete(id=None):
    if id is None:
        return "id를 입력하세요."
    else:
        user = mycol.find_one({"id":id}, {"_id":0})
        if user:
            mycol.delete_one({"id":id})
            result = list(mycol.find({}, {"_id":0}).limit(10))
            print(result)
            return result
        else:
            return f'id = {id} 데이터가 존재하지 않습니다.'
