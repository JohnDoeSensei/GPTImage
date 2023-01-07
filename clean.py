import pathlib
from module.ConfigParser import ConfigParser

config = ConfigParser()
path_json = pathlib.Path(config.get_json_dir())
path_img = pathlib.Path(config.get_img_dir())
for child in path_json.iterdir():
    if child.is_file():
        child.unlink()
for child in path_img.iterdir():
    if child.is_file():
        child.unlink()