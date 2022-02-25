from fastapi import FastAPI, Form, UploadFile, File, Body
from multipart import MultipartParser
from database import database, metadata, engine
from models import QRcode, User
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
async def qrgen(file: UploadFile = File(...)):
    return {'file': file.filename,
            'description': {
                'colored': False,
                'content': 'google.com',
                'fileb64': b'iVBORw0KGgoAAAANSUhEUgAAATYAAAE2AQAAAADDx4MEAAACRUlEQVR4nO2aS4rcMBRFz4sEPZQh\nC+ilqHbQS2qypOzAWkotoMAeNljcDCTVJ6OGgMpxSQPjKh+wHo/3u7KJ76z841sYDO7fODTf3Tlp\nDhKEDaK29ihse7fjKByagyRpQ1qAWC5ORG1IkjQPf/TksplNQHpvAZGmbKQJSGb27P29KhfPbwKc\niJJKpPR47+Buy9/dp5NDrKA0Xfxjod+7HUfinFrpyGancEtaUCLlyft7Jc7DavU+fWz+r9Coj8Lu\n7TgKVzuo1kZdGyo9rtFfdeKaPxaQlvv5o7inXfZux1E4qgNwgiBVp+CkuTzdGPHRj7tO5VuZ1CWp\nembGFUcNf3TlSkPlZJ+S7ES2oqHEpcbHk/f3UlypGnX2q7mp/lfWqB9duZql5pqWuC8dOBGXka96\nch7CxVtUNuLvnwKyCcCisokVSB+XvdtxFK51UIurXa4Wp5rDmog14qMf52F9u0WFjPBlInwZkL2K\nyDvioxdXO6jY4oOi7y5tMGmFfu92HIXzsHqAbJShsETKdhV+3Ub62L0dB+LafK6ZbHYCzOytTCJA\nNuLyP9hxIE6/pmwtUkBz+Ko/0/vQ23tyj/qu1EbzJmeV+XzUj17c/fclt6Z3bq6o7hn9bi/OQ1gA\nsiedMLF6LJ4N1fLuNnvi/l6N45qRyvc+VwGxrXocsnc7DskFyT7P/k5jrBr86K+ewq1mJSDSe1UW\nYfXYaSf7ewHO06ZAIAhYJxTPBlU5uZjSNPSSTtxDf/XQ9NaTwnE+2JWz8X37rrg/VVnC1e1cBMYA\nAAAASUVORK5CYII=\n'
'
            }}


@app.post('/qr')
async def qrgen(file: str = Form(...)):
    print(file)
    return file
