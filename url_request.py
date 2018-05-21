import threading
import urllib.request
import urllib.error

import config


class UrlRequest:

    def __init__(self, url):
        self.url = url
        self.interesting_http_codes = config.INTERESTING_HTTP_CODES
        self.extensions = config.EXTENSIONS
        self.__http_code = None
        self.is_interesting = False
        self.is_file = False
        self.__is_file()

    def do_request(self):
        try:
            with urllib.request.urlopen(self.url) as response:
                self.__http_code = response.getcode()
        except urllib.error.HTTPError as e:
            self.__http_code = e.code
        except urllib.error.URLError as e:
            pass
        finally:
            if self.__http_code in self.interesting_http_codes:
                self.is_interesting = True

    def __is_file(self):
        if self.url.endswith(tuple(self.extensions)):
            self.is_file = True

    def __str__(self):
        return self.url + '\t\t\t' + str(self.http_code)

    @property
    def response(self):
        return self.url, self.__http_code

    @property
    def http_code(self):
        return self.__http_code
