# arg utils
import argparse


def price_table_type(arg):
    valid_cols = {'open', 'close', 'high', 'low'}
    input_cols = [col.strip() for col in arg.split(',')]
    if set(input_cols) - valid_cols:
        raise argparse.ArgumentTypeError('Invalid column')
    return input_cols
