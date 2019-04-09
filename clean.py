import logging
import os
import shutil

from bin.configuration import ConfigurationResolver
from bin.parser import get_parsed_arg

FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT)
logging.getLogger().setLevel(logging.INFO)


def remove_dir_by_name(args):
    for key, value in vars(args).iteritems():
        if value is not None:
            for dirname, dirnames, filenames in os.walk(ConfigurationResolver.read_properties(key)):
                for subdirname in dirnames:
                    if subdirname == value:
                        to_rem = os.path.join(dirname, subdirname)
                        logging.info('Removing: ' + to_rem)
                        print('Removing: ' + to_rem)
                        shutil.rmtree(to_rem, ignore_errors=True)


if __name__ == "__main__":
    args = get_parsed_arg()
    remove_dir_by_name(args)
