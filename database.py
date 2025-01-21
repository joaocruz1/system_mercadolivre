from peewee import *

db = SqliteDatabase('database.db', check_same_thread=False)

class Shop(Model):
    name = CharField(unique=True)

    class Meta:
        database = db

class User(Model):
    shop = ForeignKeyField(Shop, backref='shops')
    name = CharField()
    email = CharField(unique=True)
    password = CharField()
    adm = BooleanField(default=False)

    class Meta:
        database = db
