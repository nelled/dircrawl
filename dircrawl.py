import argparse
from tabulate import tabulate
from brute_force_generator import BruteForceGenerator
from dircrawl_manager import DircrawlManager
from word_list import WordList

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('-url', required=True, help="Site to examine.")
    ap.add_argument('-words', required=False, help="Path to input file.")
    ap.add_argument('-threads', required=False, type=int, help="Number of threads.")
    ap.add_argument('-depth', required=False, type=int, help="How deep should we descend into the structure.")
    ap.add_argument('-bruteforce', dest='bruteforce', action='store_true', help="Do you want to use bruteforce?")
    ap.set_defaults(threads=20, depth=2, bruteforce=False)

    args = vars(ap.parse_args())
    url = args['url']
    if args['bruteforce']:
        word_generator = BruteForceGenerator().generator()
    elif args['words']:
        word_generator = WordList(args['words']).word_list
    else:
        print("Please set the bruteforce flag or specify a path to a text file containing words.")
        exit(0)
    dircrawl_manager = DircrawlManager(word_generator, url, args['threads'], args['depth'])
    dircrawl_manager.run()
    list_for_tabulate = [[request.url, request.http_code] for request in dircrawl_manager.results]
    print(tabulate(list_for_tabulate, headers=['URL', 'HTTP CODE'], tablefmt='grid'))
