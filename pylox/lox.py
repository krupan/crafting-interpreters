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

# TODO: maybe make an error reporter class to contain this an the next
# two functions
had_error = False

# TODO: make the error output match gcc's style:
#
#     filename:line:column: message
#
def report(line_no, where, message):
    print(f"[line {line}] Error {where}: {message}")
    had_error = True


def error(line_no, message):
    report(line_no, "", message)


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
        had_error = False


def run_file(path):
    try:
        run(open(path).read())
        if had_error:
            return 65
        return 0
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
