from cmd2 import CommandSet, with_argparser, with_default_category
import plotext as plt
from rich.table import Table

from ..args import (
    new_asset_parser,
    plot_parser,
    prices_parser
)


@with_default_category('Market')
class MarketCommandSet(CommandSet):
    
    def do_assets(self, _):
        response = self._cmd.client.get('api/indexes/')
        indexes = response.json()
        
        table = Table(title='Assets')
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


    @with_argparser(new_asset_parser())
    def do_add_asset(self, args):
        data = {'symbol': args.symbol, 'name': args.name}

        response = self._cmd.client.post('api/indexes/', data=data)
        response_json = response.json()
        self._cmd.poutput(response_json)

    def _get_prices(self, asset: str) -> dict:
        response = self._cmd.client.get(
            f'api/marketdata/?index={asset}',
        )
        # todo: add HTTP error handling
        return response.json()

   
    @with_argparser(prices_parser())
    def do_prices(self, args):
        """Show prices by symbol."""

        # todo: 
        #   * add filter by date interval (--from --to)
        #   * add previous Xd (days), Xw (weeks), Xm (months) with 1 default
        #   * add column filter ``--columns open, close, high, low``
        #   * add column for % change, absolute change

        prices = self._get_prices(args.asset)
        
        table = Table(title=f'Prices for {args.asset}')
        table.add_column('Date')
        for col in args.columns:
            table.add_column(col)
        for price in prices:
            table.add_row(
                price['date'],
                str(price['open_price']),
                str(price['close_price'])
            )

        self._cmd.console.print(table)

    
    @with_argparser(plot_parser())
    def do_plot(self, args):
        """Display a candlestick chart."""
        prices = self._get_prices(args.asset)

        # convert json to separate lists
        dates, data = [], {'Open': [], 'Close': [], 'High': [], 'Low': []}
        for price in prices:
            # 2024-01-05 -> 05/01/2024
            year, month, day = price['date'].split('-')
            dates.append(f'{day}/{month}/{year}')
            data['Open'].append(price['open_price'])
            data['High'].append(price['high_price'])
            data['Low'].append(price['low_price'])
            data['Close'].append(price['close_price'])
        
        # plt.plotsize(60, 15)
        plt.clear_data()
        plt.clear_figure()
        plt.candlestick(dates, data)
        plt.title(f'Chart for {args.asset}')
        plt.show()


    def do_watchlist(self, args):
        """View, create, or remove a watchlist."""
        pass



