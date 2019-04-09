from bin.executorsImpl import CommandExecutorImpl
from bin.parser import get_parsed_arg

if __name__ == "__main__":
    args = get_parsed_arg()
    CommandExecutorImpl().execute(args)
