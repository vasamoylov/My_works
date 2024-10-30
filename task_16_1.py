from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def wellcome() -> str:
    return f'Главная страница'


@app.get('/user/admin')
async def admin() -> str:
    return f'Вы вошли как администратор'


@app.get('/user/{user_id}')
async def users(user_id: int) -> str:
    return f'Вы вошли как пользователь № {user_id}'


@app.get('/user')
async def user_paginator(username: str, age: int) -> dict:
    return {'User': username, 'Age': age}
