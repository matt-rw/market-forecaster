from cmd2 import CommandSet, with_default_category



@with_default_category('Market')
class MarketCommandSet(CommandSet):
    
    def do_test(self, _):
        pass

    def do_list_indexes(self, _):
        response = self._cmd.client.get('indexes/')
        print(response.json())

    def do_new_index(self, _):
        pass
