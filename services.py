import base64
import qrcode
from PIL import Image
import os

DIR_MEDIA = './media/'

# todo add to db
def convert_frombase64(base: str, pathfile: str):
    decode_img = base64.decodebytes(base.encode())
    with open(pathfile, 'wb') as img:
        img.write(decode_img)
        return img


# todo add to db
def convert_tobase64(pathfile: str):
    with open(pathfile, 'rb') as img:
        encode_img = base64.encodebytes(img.read())
        return encode_img


def qr_generator(content: str = "https://google.com", name: str = '1'):
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(content)
    QRimg = qr.make_image(fill_color='black', back_color="white").convert("RGB")
    QRimg.save(name+'.png')
    path = DIR_MEDIA + name +'.png'
    print(os.path.isfile(path))
    return path

print(qr_generator())