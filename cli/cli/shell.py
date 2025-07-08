from cmd2 import Cmd
from pyfiglet import figlet_format
from httpx import Client
from rich.console import Console

from .commands.commands import MarketCommandSet
from .commands.ml import MLCommands


class MarketCLI(Cmd):
    prompt = 'market> '

    def __init__(self, host='192.168.14.128', port=8000):
        # Cmd attributes
        super().__init__()
        self.intro = figlet_format('Market CLI')
        self.default_category = 'Default'

        # self.register_command_set(MarketCommandSet())
        self.client = Client(base_url=f'http://{host}:{port}/')
        self.console = Console()
