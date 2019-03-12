# from fabric.api import run, env

from executor import Executor


class TagAndDeployExecutorImpl(Executor):
    def execute(self, directory, command):
        self.execute_command(directory, 'tag@deploy')


class GradleCommandExecutorImpl(Executor):
    def execute(self, directory, command):
        self.execute_command(directory, 'gradle', command)


class ReleaseCommandExecutorImpl(Executor):
    def __init__(self, host, shh_key):
        self.host = host
        self.shh_key = shh_key

    def execute(self, directory, command):
        print directory
        print command
        print self.host
        print self.shh_key
        # env.use_ssh_config = True
        # env.hosts = [self.host]
        # env.user = "vektor"
        # env.key_filename = self.shh_key
        # env.port = 22
        # run(command + " " + directory)
