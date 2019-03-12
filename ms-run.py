import argparse
import logging
import subprocess

import configparser

import executor
from executorsImpl import TagAndDeployExecutorImpl, GradleCommandExecutorImpl, ReleaseCommandExecutorImpl

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


def execute(args, executor):
    for key, value in vars(args).iteritems():
        if key is not 'main_command':
            if value is not None and value is not False:
                dir = get_values_by_key_from_group('sources', key)
                command = value
                executor.execute(dir, command)


def parse_arg(args):
    if args.main_command == 't&d':
        execute(args, TagAndDeployExecutorImpl())
    if args.main_command == 'run':
        execute(args, GradleCommandExecutorImpl())
    # TODO do refactoru
    if args.main_command == 'rel':
        for key, value in vars(args).iteritems():
            if key is not 'main_command':
                if value is not None and value is not False:
                    host = get_values_by_key_from_group('hosts', key)
                    ssh_key = get_values_by_key_from_group('ssh_key', 'path')
                    application_dir = get_values_by_key_from_group('autodeploy_path', key)
                    ReleaseCommandExecutorImpl(host, ssh_key).execute(application_dir, './run.sh')


def get_values_by_key_from_group(group, key):
    return config[group][key]


def main(command_line=None):
    parser = argparse.ArgumentParser(add_help=True)
    subparsers = parser.add_subparsers(dest='main_command')

    tag_deploy = subparsers.add_parser('t&d')
    tag_deploy.add_argument("--st", nargs='?')
    tag_deploy.add_argument("--sn", nargs='?')
    tag_deploy.add_argument("--sauth", nargs='?')
    tag_deploy.add_argument("--saud", nargs='?')
    tag_deploy.add_argument("--cv", nargs='?')
    # tag_deploy.add_argument("--all", nargs='?')

    release = subparsers.add_parser('rel')
    release.add_argument("--cv", action='store_true')
    release.add_argument("--st", action='store_true')
    release.add_argument("--sn", action='store_true')
    release.add_argument("--sauth", action='store_true')
    release.add_argument("--saud", action='store_true')
    # release.add_argument("--all", action='store_true')

    run = subparsers.add_parser('run')
    run.add_argument("--st", nargs='?')
    run.add_argument("--sn", nargs='?')
    run.add_argument("--sauth", nargs='?')
    run.add_argument("--saud", nargs='?')
    run.add_argument("--rd", action='store_true')
    # run.add_argument("--all", nargs='?')

    args = parser.parse_args(command_line)
    parse_arg(args)


if __name__ == "__main__":
    main()
