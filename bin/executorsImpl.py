from bin.command import Command
from bin.configuration import ConfigurationResolver
from bin.executor import Executor


class CommandExecutorImpl(Executor):

    def execute(self, args):
        if args.all is not None:
            commands = CommandResolver.get_commands_with_excluded_items(args)
        else:
            commands = CommandResolver.get_commands_by(args)
        self.execute_command(commands)


class CommandResolver:
    def __init__(self):
        pass

    # TODO refaktor
    @staticmethod
    def get_commands_by(args):
        commands = []
        for key, value in vars(args).iteritems():
            if value is not None:
                if key is not 'main_command' and key is not 'all':
                    dir = ConfigurationResolver.read_properties(key)
                    command = value
                    commands.append(Command(dir, command))
        return commands

    @staticmethod
    def get_commands_with_excluded_items(args):
        commands = []
        for key, value in vars(args).iteritems():
            if key is not 'main_command' and key is not 'all':
                if key not in ConfigurationResolver.read_excluded_item():
                    dir = ConfigurationResolver.read_properties(key)
                    command = args.all
                    commands.append(Command(dir, command))
        return commands
