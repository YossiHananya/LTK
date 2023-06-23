from .base_config import BaseConfig

class DevConfig(BaseConfig):

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'dev_database.db'