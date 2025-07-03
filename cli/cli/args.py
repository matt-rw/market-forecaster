# Command args

from cmd2 import Cmd2ArgumentParser

from .utils import price_table_type


def add_pagination(parser):
    parser.add_argument('--limit')
    parser.add_argument('--offset')
    return parser


def new_asset_parser():
    parser = Cmd2ArgumentParser()
    parser.add_argument('name')
    parser.add_argument('symbol')
    return parser


def prices_parser():
    parser = Cmd2ArgumentParser()
    parser = add_pagination(parser)
    parser.add_argument('asset')
    # todo: allow re-ordering
    # todo: add options to help
    parser.add_argument(
        '--columns',
        default=['open', 'close'],
        type=price_table_type,
        help='Display selected columns; default: open, close'
    )
    return parser


def plot_parser():
    parser = Cmd2ArgumentParser()
    parser.add_argument('asset')
    return parser
