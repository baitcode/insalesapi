from xml.etree import ElementTree
from insalesapi.objects.apiObject import ApiObject

class OptionName(ApiObject):
    def __init__(self, treeElement):
        super(OptionName, self).__init__(treeElement)

    def getTitle(self):
        return int(self.gf('title'))

    def setTitle(self, title):
        """ @rtype: L{OptionName} """
        assert isinstance(title, unicode), 'title should be unicode'
        return self.sf('title', title)

    def getPosition(self, option_name_id):
        return int(self.gf('position'))

    def setPosition(self, position):
        """ @rtype: L{OptionName} """
        assert isinstance(position, int)
        return self.sf('position', int(position))

    @classmethod
    def newOptionName(cls):
        root = ElementTree.Element('option-name')
        tree = ElementTree.ElementTree(root)
        return OptionName(tree)
