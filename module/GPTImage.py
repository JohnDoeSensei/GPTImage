import json
import openai
from module.ConfigParser import ConfigParser
from pathlib import Path
from base64 import b64decode


class GPTImage:
  def __init__(self):
      try: 
        self._config = ConfigParser()
        openai.api_key = self._config.get_api_key()
        self._json_dir = Path.cwd() / self._config.get_json_dir()
        self._img_dir = Path.cwd() / self._config.get_img_dir()
        self._filename_json = None
      except Exception as ex:
        print(ex)

  def create_img(self, prompt:str, n_img:int=1, size:str='256x256'):
    def generate_image(self):
      assert size in ['256x256', '512x512', '1024x1024'], 'Size must be 256x256, 512x512, or 1024x1024'
      response = openai.Image.create(
        prompt=prompt,
        n=n_img,
        size=size,
        response_format="b64_json",
      )
      self._json_dir.mkdir(exist_ok=True)
      self._filename_json = self._json_dir / f"{prompt[:5]}-{response['created']}.json"
      with open(self._filename_json, mode="w", encoding="utf-8") as file:
        json.dump(response, file)
    def decode_image(self):
      self._img_dir.mkdir(parents=True, exist_ok=True)
      with open(self._filename_json, mode="r", encoding="utf-8") as file:
        response = json.load(file)
      for index, image_dict in enumerate(response["data"]):
          image_data = b64decode(image_dict["b64_json"])
          image_file = self._img_dir / f"{self._filename_json.stem}-{index}.png"
          with open(image_file, mode="wb") as png:
              png.write(image_data)
      self._img_path = image_file
    generate_image(self)
    decode_image(self)