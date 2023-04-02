import argparse
import sys

from . import manager


def main():
    args = ui.cli.parse()
    manager.analyse(args)
    return 0


if __name__ == '__main__':
    sys.exit(main())
