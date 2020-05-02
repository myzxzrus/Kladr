class Configuration(object):
    DEBUG = True
    SERVER_NAME = '192.168.1.86:5000'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:zxz7870347@localhost/myzxzrus'
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:zxz7870347@localhost/kladr'
    SQLALCHEMY_BINDS = {
        'myzxzrus': 'postgresql+psycopg2://postgres:zxz7870347@localhost/myzxzrus',
        'kladr': 'postgresql+psycopg2://postgres:zxz7870347@localhost/kladr'
    }

#  файл конфигурации.



