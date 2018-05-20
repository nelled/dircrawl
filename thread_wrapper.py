import threading

from helpers.helpers import get_url_len


class ThreadWrapper(threading.Thread):
    def __init__(self, q, manager):
        self.manager = manager
        self.q = q
        threading.Thread.__init__(self)

    def run(self):
        while True:
            current_request = self.q.get()
            current_request.do_request()
            if current_request.is_interesting and \
                    current_request.url != self.manager.base_url and \
                    get_url_len(self.manager.base_url, current_request.url) <= self.manager.depth:
                print("Adding to queue\n")
                print(current_request.url)
                self.manager.add_to_queue(current_request.url)
            self.q.task_done()
            #print(self.q.qsize())
