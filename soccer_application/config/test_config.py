from .base_config import BaseConfig

class TestConfig(BaseConfig):

    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'test_database.db'
