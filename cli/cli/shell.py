from cmd2 import Cmd
from httpx import Client

from .commands import MarketCommandSet


class MarketCLI(Cmd):
    prompt = 'market> '

    def __init__(self, host='192.168.14.128', port=8000):
        super().__init__()
        # self.register_command_set(MarketCommandSet())
        self.client = Client(base_url=f'http://{host}:{port}/api/')
