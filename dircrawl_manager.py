from queue import Queue

from thread_wrapper import ThreadWrapper
from url_generator import UrlGenerator
from url_request import UrlRequest


class DircrawlManager:

    def __init__(self, word_list_path, base_url, threads, depth):
        self.word_list_path = word_list_path
        self.base_url = self.__prepare_url(base_url)
        self.threads = threads
        self.depth = depth
        self.word_list = []
        self.__read_word_list()
        self.queue = Queue()
        self.add_to_queue(self.base_url)

    def __read_word_list(self):
        with open(self.word_list_path, 'r') as file:
            for line in file:
                if line:
                    l = line.strip()
                    if not l.startswith('#'):
                        self.word_list.append(l)

    def __prepare_url(self, url):
        if url[-1] != '/':
            return url + '/'
        else:
            return url

    def add_to_queue(self, url):
        url_gen = UrlGenerator(url, self.word_list)
        for url in url_gen.generate_urls():
            #print(url)
            self.queue.put(UrlRequest(url))

    def run(self):
        for i in range(self.threads):
            t = ThreadWrapper(self.queue, self)
            t.setDaemon(True)
            t.start()

        self.queue.join()

