#!/usr/bin/env python3
import argparse
import sys


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('files', nargs='*')
    return parser.parse_args()


def run_prompt():
    print("run_prompt")


def run_file(filename):
    print("run_file: " + filename)


def main(args):
    if not args.files:
        run_prompt()
    else:
        for f in args.files:
            run_file(f)


if __name__ == '__main__':
    sys.exit(main(parse_args()))
