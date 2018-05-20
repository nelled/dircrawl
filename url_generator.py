from helpers.helpers import prepare_url


class UrlGenerator:

    def __init__(self, url, words):
        self.url = prepare_url(url)
        self.words = words

    def generate_urls(self):

        for word in self.words:
            yield self.url + word


