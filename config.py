import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(32)
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql://kaunda:kaunda@localhost/schooldb'# 'sqlite:///' + os.path.join(basedir, 'app.db')
    TESTING = os.environ.get('TESTING')
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG')

    # Database
    SQLALCHEMY_DATABASE_URI =  'mysql+pymysql://kaunda:kaunda@localhost:3307/smis'
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
