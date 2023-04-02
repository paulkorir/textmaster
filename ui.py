import models

cli = models.CLIParser(prog='tm', description='Text quality heuristics')
cli.add_argument(filename, help='name of input file')
cli.add_argument('-v', '--verbose', action='store_true', help='output verbosity')
cli.add_argument('-c', '--config-file', help='an INI-like file with configs')
