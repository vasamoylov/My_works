from fastapi import FastAPI, Body, HTTPException, Path
from typing import List, Annotated
from pydantic import BaseModel

app = FastAPI()

users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get('/users')
async def get_users() -> List[User]:
    return users


@app.post('/user/{username}/{age}')
async def user_registration(
        username: Annotated[str, Path(min_length=3, max_length=20, description='Enter username', example='Vasiliy')],
        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=75)]
) -> User:
    if any(users):
        next_id = max(users, key=lambda us: us.id).id + 1
    else:
        next_id = 1
    user = User(id=next_id, username=username, age=age)
    users.append(user)
    return user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int, username: str, age: int) -> User:
    try:
        for user in users:
            if user.id == user_id:
                user.username = username
                user.age = age
            return user
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')


@app.delete('/user/{user_id}')
async def delete_user(user_id: int):
    try:
        users.pop(user_id - 1)
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')
