import base64


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
