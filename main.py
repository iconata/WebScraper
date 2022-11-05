import sys
import os
from argument_parser import ArgumentParser
from data_extraction.collect_data import CollectData

if os.getcwd() not in sys.path:
    sys.path.insert(0, os.getcwd())

from gui.button import StartGUI


def main(args):
    if args.gui:
        StartGUI()
    else:
        collector = CollectData(args.books, args.genres, args.filters, args.keywords,
                                args.title, args.titles_json)
        collector.collect_books_data()
        collector.collection.print_all_data(args.sorting)


if __name__ == "__main__":
    parser = ArgumentParser()
    main(parser.parse_arguments())
