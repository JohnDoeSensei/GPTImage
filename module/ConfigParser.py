import configparser

class ConfigParser:
    def __init__(self, filename:str='config.cfg') -> None:
        self._config = configparser.ConfigParser()
        self._config.read(filename)
    
    def get_api_key(self):
        return self._config['Apikey']['key']
    
    def get_json_dir(self):
        return self._config['Dir']['json_dir']

    def get_img_dir(self):
        return self._config['Dir']['img_dir']