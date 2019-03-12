import subprocess
from abc import ABCMeta, abstractmethod


class Executor:
    __metaclass__ = ABCMeta

    @abstractmethod
    def execute(self, directory, command):
        pass

    def execute_command(self, directory, command, command_argument=''):
        print 'start cmd /C  ' + command + ' ' + command_argument
        # subprocess.Popen('start cmd /C  ' + command + ' ' + command_argument, shell=True, cwd=dir)
