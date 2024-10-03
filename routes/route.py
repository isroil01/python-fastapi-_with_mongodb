from fastapi import APIRouter

from models.todo import Todo
from config.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId

router = APIRouter()

# get api
@router.get('/')
async def get_todos ():
    todos = list_serial(collection_name.find())
    return todos

@router.post('/')
async def create_todos (todo:Todo):
    collection_name.insert_one(dict(todo))
    return {'message':'successfully created'}

@router.put('/{id}')
async def update_todo(id:str,todo:Todo):
    collection_name.find_one_and_update({'_id':ObjectId(id)},{'$set':dict(todo)})
    return {'message':'successfully updated'}

@router.delete('/{id}')
async def delete_todo (id:str):
    collection_name.find_one_and_delete({'_id':ObjectId(id)})
    return {'message':'successfully deleted'}