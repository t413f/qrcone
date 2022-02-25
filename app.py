from fastapi import FastAPI, Form, UploadFile, File, Body
from multipart import MultipartParser
from database import database, metadata, engine
from models import QRcode, User
from schemas import QRBase, QRIn, QROut
from typing import Optional

app = FastAPI()


metadata.create_all(engine)
app.state.database = database


@app.on_event('startup')
async def on_startup():
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()


@app.on_event('shutdown')
async def on_shutdown():
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()


@app.get('/')
async def qrgen():
    return {'message': 'hello'}


@app.post('/qrgen')
async def qrgen(file: UploadFile = File(...), colored: Optional[bool] = Form(...), content: Optional[str] = Form(...)):
    return {'file': f'{file.filename}+huy'}
            # 'colored': colored,
            # 'content': content}


@app.post('/qr')
async def qrgen(file: str = Form(...)):
    print(file)
    return file
