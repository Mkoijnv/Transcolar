# config.py
import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://vinicius:123456@127.0.0.1/transcolar'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)
