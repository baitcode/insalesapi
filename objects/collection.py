from xml.etree import ElementTree
from insalesapi.objects.api_object import ApiObject

class Collection(ApiObject):
    def __init__(self, treeElement):
        super(Collection, self).__init__(treeElement)

    def is_hidden(self):
        return bool(self._gf('is-hidden'))

    def set_is_hidden(self, hidden):
        return self._sf('is-hidden', bool(hidden))

    def get_parent_id(self):
        return int(self._gf('parent-id'))

    def set_parent_id(self, parentId):
        return self._sf('parent-id', parentId)


    def get_to_torg_mail(self):
        return bool(self._gf('to-torg-mail'))

    def set_to_torg_mail(self, val):
        return self._sf('to-torg-mail', bool(val))

    def get_to_yandex_market(self):
        return bool(self._gf('to-yandex-market'))

    def set_to_yandex_market(self, val):
        return self._sf('to-yandex-market', bool(val))

    def get_title(self):
        return bool(self._gf('title'))

    def set_title(self, title):
        return self._sf('title', title)

    def get_description(self):
        return self._gf('description')

    def set_descritption(self, description):
        return self._sf('description', description)

    def get_html_title(self):
        return self._gf('html-title')

    def set_html_title(self, title):
        return self._sf('html-title', title)

    def get_meta_description(self):
        return self._gf('meta-description')

    def set_meta_description(self, description):
        return self._sf('meta-description', description)

    def get_meta_keywords(self):
        return self._gf('meta-keywords')

    def set_meta_keywords(self, keywords):
        return self._sf('meta-keywords', keywords)

    def get_permalink(self):
        return self._gf('permalink')

    def set_permalink(self, permalink):
        return self._sf('permalink', permalink)

    def get_url(self):
        return self._gf('url')

    @classmethod
    def new_collection(cls):
        root = ElementTree.Element('collection')
        tree = ElementTree.ElementTree(root)
        return Collection(tree)