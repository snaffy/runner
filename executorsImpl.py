# from fabric.api import run, env

from executor import Executor

class GradleCommandExecutorImpl(Executor):
    def execute(self, directory, command):
        self.execute_command(directory, 'gradle', command)
