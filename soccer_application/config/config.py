import yaml
from .config_names import ConfigName
import os

class Config:

    config_dir = os.path.dirname(__file__)

    def __init__(self,config_file):
        with open(config_file,'r') as f:
            self.config_data=yaml.safe_load(f)
        
    def get(self, key, default=None):
        return self.config_data.get(key, default)
    
    @classmethod
    def from_type(cls, config_value=ConfigName.DEVELOPMENT):
        config_file=os.path.join(cls.config_dir, f'{config_value.value}.yaml')
        return cls(config_file)