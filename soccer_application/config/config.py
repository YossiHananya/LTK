import yaml
from .config_names import ConfigName
import os

class Config:

    def __init__(self,config_file):
        with open(config_file,'r') as f:
            self.config_data=yaml.safe_load(f)

    def get(self,key):
        return self.config_data.get(key)
    
    @classmethod
    def from_type(cls, config_value=ConfigName.DEVELOPMENT.value):
        config_dir = os.path.dirname(__file__)
        if config_value==ConfigName.DEVELOPMENT.value:
            config_file=os.path.join(config_dir, f'{config_value}.yaml')
            return cls(config_file)
        elif config_value==ConfigName.TESTING.value:
            config_file=os.path.join(config_dir, f'{config_value}.yaml')
            return cls(config_file)
        else:
            raise ValueError("Invalid Configuration File Name. Please choose dev or testing")