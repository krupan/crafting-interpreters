#!/usr/bin/env python3
import argparse
import sys


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('files', nargs='*')
    return parser.parse_args()


class Scanner:
    def __init__(self, source):
        self.source = source

    def scan_tokens(self):
        return []


def run(source):
    scanner = Scanner(source)
    tokens = scanner.scan_tokens()

    for token in tokens:
        print(token)


def run_prompt():
    print('Welcome to the lox interpreter.  Type ctrl-d to exit')
    while True:
        try:
            line = input("> ")
        except EOFError:
            break
        run(line)


def run_file(path):
    try:
        run(open(path).read())
    except FileNotFoundError:
        print(f'file not found: {path}')
        return -1


def main(args):
    if not args.files:
        return run_prompt()
    else:
        for f in args.files:
            ret = run_file(f)
            if ret:
                return ret


if __name__ == '__main__':
    sys.exit(main(parse_args()))
