import argparse
import logging
import subprocess
from functools import partial
from operator import is_not

import configparser

import executor
from executorsImpl import GradleCommandExecutorImpl

FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT)
logging.getLogger().setLevel(logging.INFO)

config = configparser.ConfigParser()
config.sections()
config.read('source.ini')


def getExcludedItem():
    return config.get('excluded', 'all').split(',')


def possibleValues():
    return ['cv', ]


def executeCmd(command, appName, executor):
    dir = get_values_by_key_from_group('sources', appName)
    executor.execute(dir, command)


# TODO do refaktoru
def execute(args, executor):
    if (args.all is True):
        for key, value in vars(args).iteritems():
            if value is not None:
                if key is not 'main_command' and key is not 'all':
                    if key not in getExcludedItem():
                        executeCmd(value, key, executor)
    else:
        for key, value in vars(args).iteritems():
            if value is not None:
                if key is not 'main_command' and key is not 'all':
                    executeCmd(value, key, executor)


def get_values_by_key_from_group(group, key):
    return config[group][key]


def parse_arg(args):
    execute(args, GradleCommandExecutorImpl())


def main():
    parser = argparse.ArgumentParser(add_help=True)

    parser.add_argument("--sb", nargs='?')
    parser.add_argument("--s", nargs='?')
    parser.add_argument("--st", nargs='?')
    parser.add_argument("--sn", nargs='?')
    parser.add_argument("--sauth", nargs='?')
    parser.add_argument("--saud", nargs='?')
    parser.add_argument("--cv", nargs='?')
    parser.add_argument("--all", action='store_true')

    args = parser.parse_args()
    parse_arg(args)


if __name__ == "__main__":
    main()
