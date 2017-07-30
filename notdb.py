import argparse
import sys

import writeMenu
import readMenu
import functions


#DATABASE = 'test.db'
#FAECHER = ['Deutsch', 'Musik']

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
    elif action == "extract":
        readMenu.callReadMenu()
    else:
        print("Functionality missing.")

if __name__ == '__main__':
    main()
