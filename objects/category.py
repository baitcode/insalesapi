from xml.etree import ElementTree
from insalesapi.objects.apiObject import ApiObject

class Category(ApiObject):
    def __init__(self, treeElement):
        super(Category, self).__init__(treeElement)

    def getParentId(self):
        return int(self.gf('id'))

    def getTitle(self):
        return self.gf('title')

    def getPosition(self):
        return int(self.gf('position'))

    def setParent(self, parent_id):
        """@rtype: L{Category}"""
        return self._chainExecution(lambda category: category._createField('parent-id', parent_id, dict(type='integer')))

    def setTitle(self, title):
        """@rtype: L{skychip.insales.objects.Category}"""
        return self._chainExecution(lambda category: category._createField('title', title))

    def setPosition(self, position):
        """@rtype: L{skychip.insales.objects.Category}"""
        return self._chainExecution(lambda category: category._createField('position', position, dict(type='integer')))

    @classmethod
    def newCategory(cls):
        """
        @rtype: L{Category}
        """
        root = ElementTree.Element("category")
        tree = ElementTree.ElementTree(root)
        return Category(tree)

