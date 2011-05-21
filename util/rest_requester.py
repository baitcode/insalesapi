import base64
import urllib2

class BadUrlException(Exception):
    def __init__(self, *args, **kwargs):
        super(BadUrlException, self).__init__(*args, **kwargs)

class RestRequester(object):
    def __init__(self, user, password):
        super(RestRequester, self).__init__()
        self.user = user
        self.password = password
        self.auth_header = base64.b64encode('{0}:{1}'.format(user, password))

    def prepare_url(self, url, lang):
        if not lang is None:
            url += '?lang=%s' % lang
        return url

    def post(self, url, body, lang=None):
        req = urllib2.Request(self.prepare_url(url, lang))
        print str(body)
        req.add_data(str(body))
        req.add_header('Authorization', 'Basic {0}'.format(self.auth_header))
        req.add_header('Content-Type', 'application/xml')
        assert req.get_method() == 'POST'
        print('requesting {0}'.format(url))
        return urllib2.urlopen(req)

    def post_file(self, url, body, lang=None):
        req = urllib2.Request(self.prepare_url(url, lang))
        print str(body)
        req.add_data(str(body))
        req.add_header('Authorization', 'Basic {0}'.format(self.auth_header))
        req.add_header('Content-Type', 'multipart/formdata')
        assert req.get_method() == 'POST'
        print('requesting {0}'.format(url))
        return urllib2.urlopen(req)

    def put(self, url, body, lang=None):
        req = urllib2.Request(self.prepare_url(url, lang))
        req.get_method = lambda: 'PUT'
        req.add_data(str(body))
        req.add_header('Authorization', 'Basic {0}'.format(self.auth_header))
        req.add_header('Content-Type', 'application/xml')
        assert req.get_method() == 'PUT'
        print('requesting {0}'.format(url))
        return urllib2.urlopen(req)

    def get(self, url, lang=None):
        req = urllib2.Request(self.prepare_url(url, lang))
        req.add_header('Authorization', 'Basic {0}'.format(self.auth_header))
        print('requesting {0}'.format(url))
        return urllib2.urlopen(req)

    def delete(self, url, lang=None):
        req = urllib2.Request(self.prepare_url(url, lang), 'DELETE')
        req.get_method = lambda: 'DELETE'
        req.add_header('Authorization', 'Basic {0}'.format(self.auth_header))
        print('requesting {0}'.format(url))
        opener = urllib2.build_opener(urllib2.HTTPHandler)
        assert req.get_method() == 'DELETE'
        return opener.open(req)