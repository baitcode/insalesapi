from xml.etree import ElementTree
from insalesapi.objects.api_object import ApiObject

class Category(ApiObject):
    def __init__(self, treeElement):
        super(Category, self).__init__(treeElement)

    def set_parent_id(self, parent_id):
        """@rtype: L{Category}"""
        return self._sf('parent-id', int(parent_id))

    def get_parent_id(self):
        return int(self._gf('id'))

    def get_title(self):
        return self._gf('title')

    def set_title(self, title):
        """@rtype: L{skychip.insales.objects.Category}"""
        return self._sf('title', title)

    def get_position(self):
        return int(self._gf('position'))

    def set_position(self, position):
        """@rtype: L{skychip.insales.objects.Category}"""
        return self._sf('position', position)

    @classmethod
    def new_category(cls):
        """
        @rtype: L{Category}
        """
        root = ElementTree.Element("category")
        tree = ElementTree.ElementTree(root)
        return Category(tree)