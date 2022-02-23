import ormar
from typing import Optional
from database import database, metadata

class MainMeta(ormar.ModelMeta):
    metadata = metadata
    database = database

class User(ormar.Model):
    class Meta(MainMeta):
        pass
    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=50)

class QRcode(ormar.Model):
    class Meta(MainMeta):
        pass
    id: int = ormar.Integer(primary_key=True)
    colored: str = ormar.Boolean()
    title: str = ormar.String(max_length=50)
    content: str = ormar.String(max_length=300)
    file: str = ormar.String(max_length=5000)
    user: Optional[User] = ormar.ForeignKey(User)


