from pydantic import BaseModel


class QRBase(BaseModel):
    colored: bool
    content: str


class QRIn(QRBase):
    pass


class QROut(QRBase):
    fileb64: str


class User(BaseModel):
    id: int
    name: str
    token_id: str


class UserIn(User):
    pass


class UserOut(User):
    pass
