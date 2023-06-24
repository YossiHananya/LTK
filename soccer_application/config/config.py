import yaml

class Config:

    def __init__(self,config_file):
        with open(config_file,'r') as f:
            self.config_data=yaml.safe_load(f)

    def get(self,key):
        return self.config_data.get(key)