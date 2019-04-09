import argparse


def get_parsed_arg():
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument("--sb", nargs='?')
    parser.add_argument("--s", nargs='?')
    parser.add_argument("--st", nargs='?')
    parser.add_argument("--sn", nargs='?')
    parser.add_argument("--sauth", nargs='?')
    parser.add_argument("--saud", nargs='?')
    parser.add_argument("--cv", nargs='?')
    parser.add_argument("--all", nargs='?')
    return parser.parse_args()
