import argparse
from queue import Queue

from urllib.parse import urlparse

from dircrawl_manager import DircrawlManager
from helpers.helpers import prepare_url, read_word_list
from thread_wrapper import ThreadWrapper
from url_generator import UrlGenerator
from url_request import UrlRequest

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('-url', required=True, help="Site to examine.")
    ap.add_argument('-words', required=True, help="Path to input file.")
    ap.add_argument('-threads', required=False, type=int, help="Number of threads")
    ap.add_argument('-depth', required=False, type=int, help="How deep should we descend into the structure")
    ap.set_defaults(threads=10, depth=2)

    args = vars(ap.parse_args())
    url = args['url']
    dircrawl_manager = DircrawlManager(args['words'], url, args['threads'], args['depth'])
    dircrawl_manager.run()