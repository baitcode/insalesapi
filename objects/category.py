from xml.etree import ElementTree
from insalesapi.objects.api_object import ApiObject

class Category(ApiObject):
    def __init__(self, treeElement):
        super(Category, self).__init__(treeElement)

    def setParentId(self, parent_id):
        """@rtype: L{Category}"""
        return self.sf('parent-id', int(parent_id))

    def getParentId(self):
        return int(self.gf('id'))

    def getTitle(self):
        return self.gf('title')

    def setTitle(self, title):
        """@rtype: L{skychip.insales.objects.Category}"""
        return self.sf('title', title)

    def getPosition(self):
        return int(self.gf('position'))

    def setPosition(self, position):
        """@rtype: L{skychip.insales.objects.Category}"""
        return self.sf('position', position)

    @classmethod
    def newCategory(cls):
        """
        @rtype: L{Category}
        """
        root = ElementTree.Element("category")
        tree = ElementTree.ElementTree(root)
        return Category(tree)