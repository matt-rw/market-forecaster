from cmd2 import CommandSet, with_argparser, with_default_category


@with_default_category('ML')
class MLCommands(CommandSet):

    def do_models(self, args):
        """Display a list of trained models."""

    def do_predict(self, args):
        """Predict asset value changes."""
