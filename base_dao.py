from xml.etree import ElementTree
from xml.etree.ElementTree import ParseError
from insalesapi.util.rest_requester import RestRequester


class BaseDao(object):
    def __init__(self, object_name, api_key, api_password, host):
        super(BaseDao, self).__init__()
        self.object_name = object_name
        self.requester = RestRequester(api_key, api_password)
        self.host = host

    def create(self, path, body, lang=None):
        url = 'http://{0}{1}'.format(self.host, path)
        response = self.requester.post( url, body, lang)
        return self._get_object(response)

    def create_file(self, path, body, lang=None):
        url = 'http://{0}{1}'.format(self.host, path)
        response = self.requester.post_file( url, body, lang)
        return self._get_object(response)

    def _get_object(self, response):
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

    def _prepare_url(self, path):
        return  'http://{0}{1}'.format(self.host, path)

    def update(self, path, body, lang=None):
        url = self._prepare_url(path)
        response = self.requester.put( url, body, lang)
        return self._get_object(response)

    def read(self, path, lang=None):
        url = self._prepare_url(path)
        response = self.requester.get( url, lang)
        return self._get_object(response)

    def delete(self, path, lang=None):
        url = self._prepare_url(path)
        return self.requester.delete( url, lang)