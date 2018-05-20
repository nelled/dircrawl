import threading
import urllib.request
import urllib.error


class UrlRequest:
    INTERESTING_HTTP_CODES =[200]

    def __init__(self, url):
        self.url = url
        self.__http_code = None
        self.is_interesting=False

    def do_request(self):
        try:
            with urllib.request.urlopen(self.url) as response:
                self.__http_code = response.getcode()
        except urllib.error.HTTPError as e:
            self.__http_code = e.code
        except urllib.error.URLError as e:
            pass
        finally:
            if self.__http_code in self.INTERESTING_HTTP_CODES:
                self.is_interesting = True
                #print(self.response)


    @property
    def response(self):
        return self.url, self.__http_code

    @property
    def http_code(self):
        return self.__http_code
