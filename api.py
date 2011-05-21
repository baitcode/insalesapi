import urllib2
from xml.etree.ElementTree import ParseError

__author__ = 'bait'
import base64
import httplib
import urlparse
from objects import *
from xml.etree import ElementTree

class InSalesRequester(object):
    def __init__(self, user, password):
        super(InSalesRequester, self).__init__()
        self.user = user
        self.password = password
        self.auth_header = base64.b64encode('{0}:{1}'.format(user, password))

    def prepareUrl(self, url, lang):
        if not lang is None:
            url += '?lang=%s' % lang
        return url

    def post(self, url, body, lang=None):
        req = urllib2.Request(self.prepareUrl(url, lang))
        print str(body)
        req.add_data(str(body))
        req.add_header('Authorization', 'Basic {0}'.format(self.auth_header))
        req.add_header('Content-Type', 'application/xml')
        assert req.get_method() == 'POST'
        print('requesting {0}'.format(url))
        return urllib2.urlopen(req)

    def postfile(self, url, body, lang=None):
        req = urllib2.Request(self.prepareUrl(url, lang))
        print str(body)
        req.add_data(str(body))
        req.add_header('Authorization', 'Basic {0}'.format(self.auth_header))
        req.add_header('Content-Type', 'multipart/formdata')
        assert req.get_method() == 'POST'
        print('requesting {0}'.format(url))
        return urllib2.urlopen(req)

    def put(self, url, body, lang=None):
        req = urllib2.Request(self.prepareUrl(url, lang))
        req.get_method = lambda: 'PUT'
        req.add_data(str(body))
        req.add_header('Authorization', 'Basic {0}'.format(self.auth_header))
        req.add_header('Content-Type', 'application/xml')
        assert req.get_method() == 'PUT'
        print('requesting {0}'.format(url))
        return urllib2.urlopen(req)

    def get(self, url, lang=None):
        req = urllib2.Request(self.prepareUrl(url, lang))
        req.add_header('Authorization', 'Basic {0}'.format(self.auth_header))
        print('requesting {0}'.format(url))
        return urllib2.urlopen(req)

    def delete(self, url, lang=None):
        req = urllib2.Request(self.prepareUrl(url, lang), 'DELETE')
        req.get_method = lambda: 'DELETE'
        req.add_header('Authorization', 'Basic {0}'.format(self.auth_header))
        print('requesting {0}'.format(url))
        opener = urllib2.build_opener(urllib2.HTTPHandler)
        assert req.get_method() == 'DELETE'
        return opener.open(req)
        #return urllib2.urlopen(req)

class BadUrlException(Exception):
    def __init__(self, *args, **kwargs):
        super(BadUrlException, self).__init__(*args, **kwargs)

class ApiObjectCRUDDao(object):
    def __init__(self, object_name, api_key, api_password, host):
        super(ApiObjectCRUDDao, self).__init__()
        self.object_name = object_name
        self.requester = InSalesRequester(api_key, api_password)
        self.host = host

    def create(self, path, body, lang=None):
        url = 'http://{0}{1}'.format(self.host, path)
        response = self.requester.post( url, body, lang)
        return self.getObject(response)

    def createFile(self, path, body, lang=None):
        url = 'http://{0}{1}'.format(self.host, path)
        response = self.requester.postfile( url, body, lang)
        return self.getObject(response)

    def getObject(self, response):
        buffer = response.read()
        res = list()
        try:
            tree = ElementTree.fromstring(buffer)
            if tree.tag == self.object_name:
                res.append(tree)
            else:
                res = tree.findall(self.object_name)
        except ParseError:
            print('Error while parsing last request')
        return res

    def update(self, path, body, lang=None):
        url = 'http://{0}{1}'.format(self.host, path)
        response = self.requester.put( url, body, lang)
        return self.getObject(response)

    def read(self, path, lang=None):
        url = 'http://{0}{1}'.format(self.host, path)
        response = self.requester.get( url, lang)
        return self.getObject(response)

    def delete(self, path, lang=None):
        url = 'http://{0}{1}'.format(self.host, path)
        return self.requester.delete( url, lang)

