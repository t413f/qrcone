from fastapi import FastAPI, Query, Path, Body, File, UploadFile, Form
from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional, List, Union

app = FastAPI()

#
# class ModelAi(str, Enum):
#     first = 'exp'
#     second = 'flow'
#     third = 'temp'
#
# class QrGen(BaseModel):
#     id_token: str
#     url: str
#     type: str = None
#     file: str = None
#
# @app.get('/')
# async def root():
#     return {'message': 'Hello'}
#
# @app.get('/items/{slot}')
# async def item(slot: int):
#     return {'slot': slot}
#
#
# @app.get('/models/{name_model}')
# async def get_model(name_model: ModelAi):
#     if name_model == ModelAi.first:
#         return {'res': 123}
#     elif name_model == ModelAi.second:
#         return {'res': 456}
#     return {'res': 789}
#
#
# @app.post('/qr')
# async def qr_create(qr: QrGen):
#     qr_dict = qr.dict()
#     qr_dict['file'] = 123123123
#     return {'1': '123123', **qr_dict}
#
#
# @app.post('/qr/{test}', response_model=QrGen)
# async def qr_test(qr: QrGen, test: str, q: Optional[str] = None):
#     qr_dict = qr.dict()
#     if q: qr_dict.update({'q': q})
#     return qr_dict
#
#
# @app.get('/get/')
# async def multi_get(q: Optional[List[str]] = Query(None)):
#     return {'q': q}
#
# @app.get('/get2/')
# async def multi_get2(q: Optional[List[str]] = Query(["temp", "str"]), title: str = "Query string",
#         description: str = "Query string for the items to search in the database that have a good match",):
#     return {'q': q}
#
# @app.get("/check/")
# async def read_items(q: Optional[str] = Query(None, alias="item-query", deprecated=True, include_in_schema=False)):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results
#
# @app.get("/check2/")
# async def read_items(
#     hidden_query: Optional[str] = Query(None, include_in_schema=False)
# ):
#     if hidden_query:
#         return {"hidden_query": hidden_query}
#     else:
#         return {"hidden_query": "Not found"}
#
#
# @app.get("/items/{item_id}")
# async def read_items2(
#     *, item_id: int = Path(..., title="The ID of the item to get", ge=1, le=1000), q: str
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results
#
#
#     # gt: greater than
#     # ge: greater than or equal
#     # lt: less than
#     # le: less than or equal
#
#
# ##############################################################
# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None
#
#     # EXAMPLE ###############################
#     class Config:
#         schema_extra = {
#             "example": {
#                 "name": "Foo",
#                 "description": "A very nice Item",
#                 "price": 35.4,
#                 "tax": 3.2222222222,
#             }
#         }
#
# class Item2(BaseModel):
#
#     # EXAMPLE 2 #############################
#     name: str = Field(..., example="Foo")
#     description: Optional[str] = Field(None, example="A very nice Item")
#     price: float = Field(..., example=35.4)
#     tax: Optional[float] = Field(None, example=3.2)
#
# @app.put("/item/{item_id}")
# async def update_item(item_id: int, item: Item2 = Body(..., embed=True)):
#     results = {"item_id": item_id, "item": item}
#     return results
#
# @app.put("/items/{item_id}")
# async def update_item2(
#     item_id: int,
#     item: Item = Body(
#         ...,
#         # EXAMPLE 3 #######################
#         example={
#             "name": "Foo",
#             "description": "A very nice Item",
#             "price": 35.4,
#             "tax": 3.2,
#         },
#     ),
# ):
#     results = {"item_id": item_id, "item": item}
#     return results
#
# @app.put("/items/{item_id}", response_model=Item2)
# async def update_item3(
#     *,
#     item_id: int,
#     item: Item = Body(
#         ...,
#         examples={
#             "normal": {
#                 "summary": "A normal example",
#                 "description": "A **normal** item works correctly.",
#                 "value": {
#                     "name": "Foo",
#                     "description": "A very nice Item",
#                     "price": 35.4,
#                     "tax": 3.2,
#                 },
#             },
#             "converted": {
#                 "summary": "An example with converted data",
#                 "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
#                 "value": {
#                     "name": "Bar",
#                     "price": "35.4",
#                 },
#             },
#             "invalid": {
#                 "summary": "Invalid data is rejected with an error",
#                 "value": {
#                     "name": "Baz",
#                     "price": "thirty five point four",
#                 },
#             },
#         },
#     ),
# ):
#     results = {"item_id": item_id, "item": item}
#     return results
#
# from fastapi import Cookie
#
# @app.get("/items/")
# async def read_items3(ads_id: Optional[str] = Cookie(None)):
#     return {"ads_id": ads_id}

# class UserBase(BaseModel):
#     username: str
#     email: str
#     full_name: Optional[str] = None
#
#
# class UserIn(UserBase):
#     password: str
#
#
# class UserOut(UserBase):
#     pass
#
#
# class UserInDB(UserBase):
#     hashed_password: str
#
#
# def fake_password_hasher(raw_password: str):
#     return "supersecret" + raw_password
#
#
# def fake_save_user(user_in: UserIn):
#     hashed_password = fake_password_hasher(user_in.password)
#     user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
#
#     print("User saved! ..not really")
#     print(user_in_db.dict())
#     print(user_in.dict())
#     return user_in_db
#
#
# @app.post("/user/", response_model=UserOut)
# async def create_user(user_in: UserIn):
#     user_saved = fake_save_user(user_in)
#     return user_saved

# class BaseItem(BaseModel):
#     description: str
#     type: str
#
#
# class CarItem(BaseItem):
#     type = "car"
#
#
# class PlaneItem(BaseItem):
#     type = "plane"
#     size: int
#
#
# items = {
#     "item1": {"description": "All my friends drive a low rider", "type": "car"},
#     "item2": {
#         "description": "Music is my aeroplane, it's my aeroplane",
#         "type": "plane",
#         "size": 5,
#     },
# }
#
#
# @app.get("/items/{item_id}", response_model=Union[PlaneItem, CarItem])
# async def read_item(item_id: str):
#     return items[item_id]


# class Item(BaseModel):
#     name: str
#     description: str
#
#
# items = [
#     {"name": "Foo", "description": "There comes my hero"},
#     {"name": "Red", "description": "It's my aeroplane"},
# ]
#
#
# @app.get("/items/", response_model=List[Item])
# async def read_items():
#     return items


# @app.post("/files/")
# async def create_file(file: bytes = File(..., description="A file read as bytes")):
#     return {"file_size": len(file)}
#
#
# @app.post("/uploadfile/")
# async def create_upload_file(
#     file: UploadFile = File(..., description="A file read as UploadFile")
# ):
#     return {"filename": file.filename}

from fastapi.responses import HTMLResponse



# @app.post("/files/")
# async def create_file(
#     file: bytes = File(...), fileb: str = Body(...), token: str = Form(...)
# ):
#     with open('res.png', 'wb') as f:
#         f.write(file)
#     return {
#         "file_size": len(file),
#         "token": token,
#         "fileb_content_type": fileb.content_type,
#     }

