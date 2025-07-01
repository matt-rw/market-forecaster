# Command args

from cmd2 import Cmd2ArgumentParser


def new_index_parser():
    parser = Cmd2ArgumentParser()
    parser.add_argument('name')
    parser.add_argument('symbol')

    return parser


def prices_parser():
    parser = Cmd2ArgumentParser()
    parser.add_argument('index')

    return parser
