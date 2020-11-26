import argparse
import collections
import configparser
import hashlib
import os
import re
import sys
import zlib
from cmd import repo_create

argparser = argparse.ArgumentParser(description="The easy VCS")
argsubparser = argparser.add_subparsers(title="Command", dest="command")
argsubparser.required = True

argsp = argsubparser.add_parser(
    "init", help="Initialize a new, empty VCS Repository")
argsp.add_argument(
    "path",
    metavar="directory",
    nargs="?",
    default=".",
    help="Where to create the repository"
)

def cmd_init(args):
    repo_create(args.path)


def main(argv=sys.argv[1:]):
    args = argparser.parse_args(argv)
    if args.command == "init":
        cmd_init(args)


if __name__ == "__main__":
    main()