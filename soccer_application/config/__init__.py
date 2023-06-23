import os
from .base_config import BaseConfig
from .test_config import TestConfig
from .dev_config import DevConfig

def get_config():
    environment = os.getenv('FLASK_ENV', 'development')
    if environment == 'production':
        return BaseConfig()
    elif environment == 'testing':
        return TestConfig()
    else:
        return DevConfig()

