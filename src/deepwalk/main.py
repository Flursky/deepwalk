# -*- coding: utf-8 -*-
"""
This is a skeleton file that can serve as a starting point for a Python
console script. To run this script uncomment the following lines in the
[options.entry_points] section in setup.cfg:

    console_scripts =
         fibonacci = deepwalk.skeleton:run

Then run `python setup.py install` which will install the command `fibonacci`
inside your current environment.
Besides console scripts, the header (i.e. until _logger...) of this file can
also be used as template for Python modules.

Note: This skeleton file can be safely removed if not needed!
"""

import argparse
import sys
import logging

from deepwalk import __version__

__author__ = "Flursky"
__copyright__ = "Flursky"
__license__ = "mit"

_logger = logging.getLogger(__name__)


def fib(n):
    """Fibonacci example function

    Args:
      n (int): integer

    Returns:
      int: n-th Fibonacci number
    """
    assert n > 0
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a+b
    return a


def parse_args(args):
    """Parse command line parameters

    Args:
      args ([str]): command line parameters as list of strings

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(
        description="Training a DeepWalk model")
    parser.add_argument(
        "--version",
        action="version",
        version="deepwalk {ver}".format(ver=__version__))
    parser.add_argument(
        "--edge-list",
        help="Edge file for constructing the graph",
        type=str
    )
    parser.add_argument(
        "--oriented",
        help="If the graph is oriented or not",
        type=bool,
        default=False
    )
    parser.add_argument(
        "--num-walk",
        help="Number of walks per node",
        type=int,
    )
    parser.add_argument(
        "--walk-length",
        help="Walk length",
        type=int
    )
    parser.add_argument(
        "window-size",
        help="Skip-Gram parameter (default = 5)",
        type=int,
        default=5
    )
    parser.add_argument(
        "--embed-size",
        help="Output vector size (default = 128)",
        type=int,
        default=128
    )
    parser.add_argument(
        "--workers",
        help="Word2Vec parameter: number of workers used (default = 1)",
        type=int,
        default=1
    )

    parser.add_argument(
        "--epochs",
        help="Number of training epochs (default = 10)",
        type=int,
        default=10
    )
    parser.add_argument(
        "-v",
        "--verbose",
        dest="loglevel",
        help="set loglevel to INFO",
        action="store_const",
        const=logging.INFO)
    parser.add_argument(
        "-vv",
        "--very-verbose",
        dest="loglevel",
        help="set loglevel to DEBUG",
        action="store_const",
        const=logging.DEBUG)
    return parser.parse_args(args)


def setup_logging(loglevel):
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(level=loglevel, stream=sys.stdout,
                        format=logformat, datefmt="%Y-%m-%d %H:%M:%S")


def main(args):
    """Main entry point allowing external calls

    Args:
      args ([str]): command line parameter list
    """
    args = parse_args(args)
    setup_logging(args.loglevel)
    _logger.debug("Starting crazy calculations...")
    print("The {}-th Fibonacci number is {}".format(args.n, fib(args.n)))
    _logger.info("Script ends here")


def run():
    """Entry point for console_scripts
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
