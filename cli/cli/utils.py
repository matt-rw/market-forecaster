# arg utils
from argparse import ArgumentTypeError


def price_table_type(arg):
    valid_cols = {'open', 'close', 'high', 'low'}
    input_cols = [col.strip() for col in arg.split(',')]
    if set(input_cols) - valid_cols:
        raise ArgumentTypeError('Invalid column')
    return input_cols


def price_time_type(arg):
    """Validate unit for days, weeks, or months.

    Example:
        1d is one day, 5m is five months.

    Returns:
        Tuple(int, str): duration and unit
    
    Raises:
        ArgumentTypeError    
    """
    num = ''
    unit = ''
    for char in arg:
        if char.isnumeric() and not unit:
            num += char
        elif char.lower() in ['d', 'w', 'm']:
            unit = char
        else:
            raise ArgumentTypeError('Invalid time unit')
    if not num or not unit:
        raise ArgumentTypeError('Invalid time unit')
    return int(num), unit
