from xml.etree import ElementTree
from xml.etree.ElementTree import ParseError
from insalesapi.util.RESTRequester import RESTRequester


class BaseDao(object):
    def __init__(self, object_name, api_key, api_password, host):
        super(BaseDao, self).__init__()
        self.object_name = object_name
        self.requester = RESTRequester(api_key, api_password)
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