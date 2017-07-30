import argparse
import sys

import writeMenu
import functions

DATABASE = 'test.db'
FAECHER = ['Deutsch', 'Musik']

def cli():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-a", "--add", help="Add a new entry to the database.",
                        action="store_true")
    group.add_argument("-x", "--extract", help="Extract data from the database.",
                        action="store_true")
    args = parser.parse_args()
    if args.add:
        return "add"
    elif args.extract:
        return "extract"
    else:
        parser.print_help()
        sys.exit(0)

def main():
    
    action = cli()
    if action == "add":
        writeMenu.callWriteMenu()
    else:
        print("Functionality not implemented yet. Sorry.")
        sys.exit(1)

if __name__ == '__main__':
    main()
