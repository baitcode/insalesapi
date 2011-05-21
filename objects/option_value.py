from insalesapi.objects.api_object import ApiObject
from xml.etree import ElementTree

class OptionValue(ApiObject):
    def __init__(self, treeElement):
        super(OptionValue, self).__init__(treeElement)

    def getTitle(self):
        return int(self.gf('title'))

    def setTitle(self, title):
        """ @rtype: L{OptionValue} """
        assert isinstance(title, unicode), 'title should be unicode'
        return self.sf('title', title)

    def getPosition(self, option_name_id):
        return int(self.gf('position'))

    def setPosition(self, position):
        """ @rtype: L{OptionValue} """
        assert isinstance(position, int)
        return self.sf('position', int(position))

    def getOptionNameId(self, option_name_id):
        return int(self.gf('option-name-id'))

    def setOptionNameId(self, option_name_id):
        """ @rtype: L{OptionValue} """
        return self.sf('option-name-id', int(option_name_id))

    @classmethod
    def newOptionValue(cls):
        root = ElementTree.Element('option-value')
        tree = ElementTree.ElementTree(root)
        return OptionValue(tree)
