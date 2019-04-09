class Command:
    def __init__(self, dir, command, arguments=''):
        self.dir = dir
        self.command = command
        self.arguments = arguments

    def get_dir(self):
        return self.dir

    def get_arguments(self):
        return self.arguments

    def get_command(self):
        return self.command
