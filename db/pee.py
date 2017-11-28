from peewee import *
db = SqliteDatabase('licitacao.db')
db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Fornecedor(BaseModel):
    name = CharField()
    email = CharField()
    passwd = CharField()

class Licitacao(BaseModel):
    applicant = CharField()
    supplier = CharField()
    lowest_bid = IntegerField()
    products = CharField()
    start_date = CharField()
    end_date = CharField()
