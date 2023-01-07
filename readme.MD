# GPT Image

GPT Image is a Python program to generate image from text.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install GPT Image.

```bash
pip install -r requirements.txt
```

-Visit [Openai.com](https://openai.com/api/) and create an account.
-Fill line in **config.cfg**:
`` key=<YOUR API KEY WITHOUT QUOTE> ``

## Usage

To generate one image of funny meme in 512x512 resolution: 

```bash
.\main.py  -n 1 -s 512x512 "Beautiful view from drone on lake"
```

For help:
```bash
.\main.py -h
```

## Result :
![Beautiful view from drone on lake!](\images\Beaut-1673053145-0.png "watch out")

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)