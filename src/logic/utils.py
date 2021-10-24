import os
import yaml
import pathlib


class Singleton(type):
    _instance = None
    def __call__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance


class ConfigManager(metaclass=Singleton):
    @staticmethod
    def load_config():
        with open(os.path.join(pathlib.Path(__file__).parent.resolve(), "config.yaml"), "r") as config:
            return yaml.safe_load(config)


class SerializableDict:
    def __init__(self, **kwargs) -> None:
        self.__dict__.update(kwargs)