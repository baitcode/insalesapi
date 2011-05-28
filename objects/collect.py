from xml.etree import ElementTree
from insalesapi.objects.api_object import ApiObject

class Collect(ApiObject):
    def __init__(self, treeElement):
        super(Collect, self).__init__(treeElement)

    def set_collection_id(self, collection_id):
        return self._sf('collection-id', int(collection_id))

    def get_collection_id(self):
        try:
            return int(self._gf('collect-id'))
        except TypeError:
            return -1

    def set_product_id(self, product_id):
        return self._sf('product-id', int(product_id))

    def get_product_id(self):
        try:
            return int(self._gf('product-id'))
        except TypeError:
            return -1

    @classmethod
    def newCollect(cls):
        root = ElementTree.Element('collect')
        tree = ElementTree.ElementTree(root)
        return Collect(tree)
