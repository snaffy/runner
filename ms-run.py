import argparse
import logging
import subprocess

import configparser

FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT)
logging.getLogger().setLevel(logging.INFO)

config = configparser.ConfigParser()
config.sections()
config.read('source.ini')


def run(command, dir, preCommand='gradle'):
    subprocess.Popen('start cmd /C  ' + preCommand + ' ' + command, shell=True, cwd=dir)


def getExcludedItem():
    return config.get('excluded', 'all').split(',')


def parse_arg(args):
    if args.st:
        dir = config['sources']['trial']
        command = args.st
        run(command, dir)
    if args.sn:
        dir = config['sources']['not']
        command = args.sn
        run(command, dir)
    if args.sauth:
        dir = config['sources']['auth']
        command = args.sauth
        run(command, dir)
    if args.saud:
        dir = config['sources']['auditing']
        command = args.saud
        run(command, dir)
    if args.all:
        v = dict(config.items('sources'))
        excluded = getExcludedItem()
        command = args.all
        for key, value in v.iteritems():
            if key not in excluded:
                dir = config['sources'][key]
                run(command, dir)
    if args.rd:
        dir = config['other']['redis']
        command = 'redis-server.exe'
        run(command, dir, '')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--st", nargs='?')
    parser.add_argument("--sn", nargs='?')
    parser.add_argument("--sauth", nargs='?')
    parser.add_argument("--saud", nargs='?')
    parser.add_argument("--rd", action='store_true')
    parser.add_argument("--all", nargs='?')
    args = parser.parse_args()
    parse_arg(args)
