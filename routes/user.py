from fastapi import APIRouter, HTTPException
from models.user import User
from bson import ObjectId
from config.db import conn
from schemas.user import userEntity, usersEntity

user = APIRouter()
@user.get('/')
async def find_all_users():
    print(conn.local.user.find())
    print(usersEntity(conn.local.user.find()))
    return usersEntity(conn.local.user.find())

@user.post('/')
async def Create_users(user : User):
    conn.local.user.insert_one(dict(user))
    return(usersEntity(conn.local.user.find()))

@user.get('/{id}')
async def find_user(id: str):
    user = conn.local.user.find_one({"_id":ObjectId(id)})
    if user:
        return userEntity(user)
    else:
        return ("User not found")
        

@user.put('/{id}')
async def update_user(id: str, user: User):
    conn.local.user.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(user)})
    updated_user = conn.local.user.find_one({"_id": ObjectId(id)})
    if updated_user:
        return userEntity(updated_user)
    else:
        raise HTTPException(status_code=404, detail="User not found")

@user.delete('/{id}')
async def delete_user(id: str):
    deleted_user = conn.local.user.find_one_and_delete({"_id": ObjectId(id)})
    if deleted_user:
        return userEntity(deleted_user)
    else:
        raise HTTPException(status_code=404, detail="User not found")