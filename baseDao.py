from xml.etree import ElementTree
from xml.etree.ElementTree import ParseError
from insalesapi.util.restRequester import RestRequester


class BaseDao(object):
    def __init__(self, object_name, api_key, api_password, host):
        super(BaseDao, self).__init__()
        self.object_name = object_name
        self.requester = RestRequester(api_key, api_password)
        self.host = host

    def create(self, path, body, lang=None):
        url = 'http://{0}{1}'.format(self.host, path)
        response = self.requester.post( url, body, lang)
        return self._getObject(response)

    def createFile(self, path, body, lang=None):
        url = 'http://{0}{1}'.format(self.host, path)
        response = self.requester.postfile( url, body, lang)
        return self._getObject(response)

    def _getObject(self, response):
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

    def _prepareUrl(self, path):
        return  'http://{0}{1}'.format(self.host, path)

    def update(self, path, body, lang=None):
        url = self._prepareUrl(path)
        response = self.requester.put( url, body, lang)
        return self._getObject(response)

    def read(self, path, lang=None):
        url = self._prepareUrl(path)
        response = self.requester.get( url, lang)
        return self._getObject(response)

    def delete(self, path, lang=None):
        url = self._prepareUrl(path)
        return self.requester.delete( url, lang)