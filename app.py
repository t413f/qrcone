from fastapi import FastAPI, Form, UploadFile, File, Body
from database import database, metadata, engine
from models import QRcode
from schemas import QRBase, QRIn, QROut

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
async def qrgen(description: QRIn = Body(...)):
    print(description.dict())
    return description