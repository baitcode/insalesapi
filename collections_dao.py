from insalesapi.base_dao import BaseDao
from insalesapi.objects.collection import Collection


class CollectionsDao(BaseDao):
    def __init__(self, api_key, api_password, host):
        super(CollectionsDao, self).__init__('collection', api_key, api_password, host)

    def get_list(self, lang=None):
        """@rtype: L{list}"""
        collections = self.read('/admin/collections.xml', lang)
        return Collection.wrapCollection(collections)

    def get(self, id, lang=None):
        """@rtype: L{list}"""
        collections = self.read('/admin/collections/%d' % id, lang)
        return Collection.wrapCollection(collections)

    def edit(self, category, lang=None):
        """@rtype: L{list}"""
        collections = self.update('/admin/collections/%d' % int(category.get_id()), category, lang)
        return Collection.wrapCollection(collections)

    def add(self, category, lang=None):
        collections = self.create('/admin/collections.xml', category, lang)
        return Collection.wrapCollection(collections)

    def remove(self, id, lang=None):
        return self.delete('/admin/collections/%d' % id, lang)