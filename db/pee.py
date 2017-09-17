from peewee import *
db = SqliteDatabase('fornecedor.db')
db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Fornecedor(BaseModel):
    name = CharField()
    email = CharField()
    passwd = CharField()
