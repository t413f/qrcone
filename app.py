from fastapi import FastAPI, Form, UploadFile, File, Body, Depends
from multipart import MultipartParser
from database import database, metadata, engine
from models import QRcode, User
from schemas import QRBase, QRIn, QROut
from typing import Optional
from pydantic import BaseModel

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
async def qrgen(file: UploadFile = File(...), desc: QRIn = Depends()):
    return {'file': file.filename,
            **desc.dict()}
            # 'colored': colored,
            # 'content': content}


class QRBase(BaseModel):
    colored: bool = Form(False)
    content: str = Form("sadmwkemfwkemfwe")
    file: UploadFile = File(...)

@app.post('/qr')
async def qrgen(qr: QRBase = Depends()):
    print(qr.dict())
    return {'file': qr.file.filename+"huy"}
