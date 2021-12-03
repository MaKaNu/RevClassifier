# Builtin imports
from pathlib import Path
import json

# Thirdparty imports
from pydantic import BaseModel
from pydantic.class_validators import validator


class Config(BaseModel):
    path = Path("")

    def load_json(self, config_file=Path("revclassifier/config.json")):
        with config_file.open() as json_file:
            config_data = json.load(json_file)
            self.path = config_data['config']['path']
            print(self.path)

    @validator('path')
    def check_path_existence(cls, val):
        if not val.is_dir():
            msg = colored(255, 85, 85, f"Directory \"{val}\" does not exists")
            raise ValueError(msg)
        return val


def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)
