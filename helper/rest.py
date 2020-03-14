import support.test_data2 as TD
import requests


class Builder(object):
    def __init__(self, url):
        self._url = url
        self.reset()
        
    def reset(self):
        self._request = Request()
        self._request._body = { }
        self._request._head = { }
        return self

    def __getattr__(self, name):
        self._request.add(name)
        return self

    def body(self, **kwargs):
        self._request._body = kwargs
        print(self._request._body)
        return self

    def head(self, **kwargs):
        self._request._head = kwargs
        return self

    def url(self):
        path = '/' + '/'.join(self._request._parts)
        return self._url + path


class Request:
    def __init__(self):
        self._parts = []
        self._body = { }

    def add(self, url):
        self._parts.append(url)


class Get(Builder):
    def perf(self):
        if not self._request._head:
            return requests.get(self.url(), headers=TD.headers())
        else:
            return requests.get(self.url(), headers=self._request._head)

class Post(Builder):
    def perf(self):
        if not self._request._head:
            return requests.post(self.url(), json=self._request._body, headers=TD.headers())
        else:
            return requests.post(self.url(), json=self._request._body, headers=self._request._head)
