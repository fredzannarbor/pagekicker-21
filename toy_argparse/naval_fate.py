"""Naval Fate.

Usage:
  naval_fate.py ship new <name>...
  naval_fate.py ship <name> [--speed=<kn>]
  naval_fate.py (-h | --help)
  naval_fate.py --version


Options:
  -h --help     Show this screen.
  --version     Show version.
  --speed=<kn>  Speed in knots [default: 10].
  --uuid=VALUE

"""
from docopt import docopt


if __name__ == '__main__':
    arguments = docopt(__doc__, version='Naval Fate 2.0')
    print(arguments)