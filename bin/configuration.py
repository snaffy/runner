import configparser
import os
config = configparser.ConfigParser()
config.sections()
config.read(os.path.dirname(__file__) + '/../source.ini')


class ConfigurationResolver:

    def __init__(self):
        pass

    @staticmethod
    def read_properties(key, group='sources'):
        return config[group][key]

    @staticmethod
    def read_excluded_item():
        return ConfigurationResolver.read_properties('all', 'excluded').split(',')
