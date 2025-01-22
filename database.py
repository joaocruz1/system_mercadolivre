from peewee import *
from flask_login import UserMixin

db = SqliteDatabase('database.db', check_same_thread=False)

class Shop(Model):
    name = CharField(unique=True)

    class Meta:
        database = db

class User(UserMixin, Model):
    shop = ForeignKeyField(Shop, backref='shops')
    name = CharField()
    email = CharField(unique=True)
    password = CharField()
    adm = BooleanField(default=False)

    class Meta:
        database = db

    # Método is_active necessário para Flask-Login
    @property
    def is_active(self):
        # Retorna True para indicar que o usuário está ativo
        return True