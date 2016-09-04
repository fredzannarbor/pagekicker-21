"""pk_docopt

Usage:
  pk_docopt.py [--uuid="val"] [--infile="val"] [--outfile="val"]
  pk_docopt.py (-h | --help)
  pk_docopt.py --version


Options:
  -h --help     Show this screen.
  --version     Show version.
  --uuid=<val>  Job directory
  --infile=<file> input file
  --outfile=<file>


"""
from docopt import docopt


if __name__ == '__main__':
    arguments = docopt(__doc__, version='Naval Fate 2.0')
    print(arguments)