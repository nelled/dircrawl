from helpers.helpers import prepare_url
import config


class UrlGenerator:
    def __init__(self, url, words):
        self.extensions = config.EXTENSIONS
        self.url = prepare_url(url)
        self.words = words

    def generate_dir_names(self):
        for word in self.words:
            yield self.url + word + '/'

    def generate_file_names(self):
        for word in self.words:
            for extension in self.extensions:
                yield self.url + word + extension
