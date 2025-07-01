from cmd2 import CommandSet, with_argparser, with_default_category
from rich.table import Table

from .args import new_index_parser


@with_default_category('Market')
class MarketCommandSet(CommandSet):
    
    def do_list_indexes(self, _):
        response = self._cmd.client.get('api/indexes/')
        indexes = response.json()
        
        table = Table(title='Indexes')
        table.add_column('ID', justify='center', style='yellow')
        table.add_column('Symbol', justify='center', style='cyan')
        table.add_column('Name', justify='center', style='cyan')
        for num, index in enumerate(indexes):
            table.add_row(
                str(index['id']),
                index['symbol'],
                index['name']
            )
        self._cmd.console.print(table)


    @with_argparser(new_index_parser())
    def do_new_index(self, args):
        data = {'symbol': args.symbol, 'name': args.name}

        response = self._cmd.client.post('api/indexes/', data=data)
        response_json = response.json()
        self._cmd.poutput(response_json)]
    
    def do_prices(self, args):
        """Show prices by index or date."""
        if args.index:
            pass
        data = {
            'index': args.index
        }

        response = self._cmd.client.get(
            'api/marketdata',
            data=data
        }
        print(response.json())


