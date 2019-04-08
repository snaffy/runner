import argparse
import os
import shutil

import configparser

config = configparser.ConfigParser()
config.sections()
config.read('source.ini')


def get_values_by_key_from_group(group, key):
    return config[group][key]

def parse_arg(args):
    for key, value in vars(args).iteritems():
        if value is not None:
            for dirname, dirnames, filenames in os.walk(get_values_by_key_from_group('sources', key)):
                for subdirname in dirnames:
                    if (subdirname == value):
                        to_rem = os.path.join(dirname, subdirname)
                        print('Removing: ' + to_rem)
                        shutil.rmtree(to_rem, ignore_errors=True)

def main():
    parser = argparse.ArgumentParser(add_help=True)

    parser.add_argument("--sb", nargs='?')
    parser.add_argument("--s", nargs='?')
    parser.add_argument("--st", nargs='?')
    parser.add_argument("--sn", nargs='?')
    parser.add_argument("--sauth", nargs='?')
    parser.add_argument("--saud", nargs='?')
    parser.add_argument("--cv", nargs='?')

    args = parser.parse_args()
    parse_arg(args)


if __name__ == "__main__":
    main()
