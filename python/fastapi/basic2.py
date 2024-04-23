from fastapi import FastAPI
from pydantic.main import BaseModel

class HelloWorldRequest(BaseModel):
    name : str
    age : int

app = FastAPI()

@app.get('/')
async def Hello():
    return "Hello World~!!"

@app.get(path='/hello/{name}')
async def hello_with_name(name:str):
    return "Hello with name. your name is"+name

@app.get(path='/hello/query')
async def hello_with_querystring(name:str):
    return "Hello with name. your name is"+name

@app.get(path='/hello/post')
async def hello_post(request: HelloworldRequest):
     return "Hello with name. your name is {}, your age is P{}".format(request.name, request.age)

