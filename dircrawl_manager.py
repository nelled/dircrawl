from queue import Queue

from thread_wrapper import ThreadWrapper
from url_generator import UrlGenerator
from url_request import UrlRequest


class DircrawlManager:

    def __init__(self, word_generator, base_url, threads, depth):
        self.word_generator = word_generator
        self.base_url = self.__prepare_url(base_url)
        self.threads = threads
        self.depth = depth
        self.queue = Queue()
        self.run()
        self.add_to_queue(self.base_url)
        self.results = []

    def __prepare_url(self, url):
        if url[-1] != '/':
            return url + '/'
        else:
            return url

    def add_to_queue(self, url):
        url_gen = UrlGenerator(url, self.word_generator)
        for url in url_gen.generate_dir_names():
            self.queue.put(UrlRequest(url))
        for url in url_gen.generate_file_names():
            self.queue.put(UrlRequest(url))


    def run(self):
        for i in range(self.threads):
            t = ThreadWrapper(self.queue, self)
            t.setDaemon(True)
            t.start()

        self.queue.join()
