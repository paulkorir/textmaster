import argparse
import sys

from . import managers, ui


def main():
    args = ui.parser.parse()
    manager.analyse(args)
    return 0


if __name__ == '__main__':
    sys.exit(main())
