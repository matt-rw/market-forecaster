# Command args

from cmd2 import Cmd2ArgumentParser as ArgumentParser


def new_index_parser():
    parser = ArgumentParser()
    parser.add_argument('name')
    parser.add_argument('symbol')

    return parser

