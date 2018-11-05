import argparse
import re

def read_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', help='pattern', required=True)
    parser.add_argument('-t', help='target', required=True)
    return parser.parse_args()


def extract():
    args = read_args()
    regex = re.compile(args.p)
    return regex.findall(args.t)


if __name__ == '__main__':
    print extract()

