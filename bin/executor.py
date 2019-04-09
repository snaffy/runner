import logging
import subprocess
from abc import ABCMeta, abstractmethod

FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT)
logging.getLogger().setLevel(logging.INFO)


class Executor:
    __metaclass__ = ABCMeta

    def execute_command(self, commands):
        for command in commands:
            logging.info(
                'cwd to: ' + command.get_dir() + ' and execute: ' + 'start cmd /C ' + command.get_command() + ' with arguments: ' + command.get_arguments())
            subprocess.Popen('start cmd /C  ' + command.get_command() + ' ' + command.get_arguments(),
                             shell=True,
                             cwd=command.get_dir())
