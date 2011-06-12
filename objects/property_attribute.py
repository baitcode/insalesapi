from xml.etree import ElementTree
from insalesapi.objects.api_object import ApiObject

class PropertyAttribute(ApiObject):
    def __init__(self, treeElement):
        super(PropertyAttribute, self).__init__(treeElement)

    def get_title(self):
        return self._gf('title')

    def set_title(self, title):
        """@rtype: L{Product}"""
        return self._sf('title', title)

    def get_value(self):
        return self._gf('value')

    def set_value(self, value):
        """@rtype: L{Product}"""
        return self._sf('value', value)

    @classmethod
    def new_property_attribute(cls):
        root = ElementTree.Element("properties-attribute")
        tree = ElementTree.ElementTree(root)
        return PropertyAttribute(tree)