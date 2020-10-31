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
from deepwalk.train import train, save_model


__author__ = "Flursky"
__copyright__ = "Flursky"
__license__ = "mit"

_logger = logging.getLogger(__name__)



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
        type=str,
        required=True
    )
    parser.add_argument(
        "--oriented",
        help="If the graph is oriented or not",
        type=bool,
        default=False
    )
    parser.add_argument(
        "--num-walks",
        help="Number of walks per node",
        type=int,
        required=True
    )
    parser.add_argument(
        "--walk-length",
        help="Walk length",
        type=int,
        required=True
    )
    parser.add_argument(
        "--window-size",
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
        "--output",
        help="Where to store embeddings",
        type=str,
        required=True
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

    edge_file = args.edge_list
    oriented = args.oriented
    num_walks = args.num_walks
    walk_length = args.walk_length
    window_size = args.window_size
    embed_size = args.embed_size
    workers = args.workers
    epochs = args.epochs
    output = args.output

    setup_logging(args.loglevel)
    
    model = train(edge_file, oriented, num_walks, walk_length, epochs, embed_size, window_size, workers)
    
    save_model(model, output)

def run():
    """
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
