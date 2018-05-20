import argparse

from urllib.parse import urlparse

from helpers.helpers import prepare_url, read_word_list
from url_generator import UrlGenerator
from url_request import UrlRequest

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('-url', required=True, help="Site to examine.")
    ap.add_argument('-words', required=True, help="Path to input file.")
    ap.add_argument('-threads', required=False, type=int, help="Number of threads")
    ap.set_defaults(threads=10)

    args = vars(ap.parse_args())
    url = args['url']
    word_list = read_word_list(args['words'])

    url_gen = UrlGenerator(url, word_list)
    threads = []
    for url in url_gen.generate_urls():
        request = UrlRequest(url)
        threads.append(request)
        request.start()

    for thread in threads:
        thread.join()
        #print(thread.response)


