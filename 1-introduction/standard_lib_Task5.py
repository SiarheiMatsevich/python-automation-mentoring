from prettytable import PrettyTable
import os
import argparse
import sys


def show_dir(path):
    out = PrettyTable()
    out.field_names = ['Mode', 'Owner', 'Group', 'Size', 'File name']
    directory = os.listdir(path)
    abs_paths = zip(directory, map(lambda f: os.path.join(path, f), directory))
    for file_name, abs_path in abs_paths:
        properties = os.stat(abs_path)
        out.add_row((properties.st_mode,
                     properties.st_uid,
                     properties.st_gid,
                     properties.st_size,
                     file_name))
    return out


def parse_cmd_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', nargs='?', default=os.getcwd(), help='Specify directory you want to show')
    if len(sys.argv) > 2:
        parser.print_help(sys.stderr)
        sys.exit(1)
    else:
        arg, _ = parser.parse_known_args()
        return arg.path


if __name__ == '__main__':
    path = parse_cmd_args()
    print(show_dir(path))
