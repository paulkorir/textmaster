import shlex
import sys

import models

parser = models.CLIParser(prog='tm', description='Text quality heuristics')
parser.add_argument('filename', help='name of input file')
parser.add_argument('-v', '--verbose', action='store_true', help='output verbosity')
parser.add_argument('-c', '--config-file', default='./textmaster.toml', help='an INI-like file with configs')


def cli(command):
    """Simulate a CLI"""
    sys.argv = shlex.split(command)
    return parser.parse_args()
