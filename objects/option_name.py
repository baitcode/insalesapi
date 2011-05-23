from xml.etree import ElementTree
from insalesapi.objects.api_object import ApiObject


class OptionName(ApiObject):
    def __init__(self, treeElement):
        super(OptionName, self).__init__(treeElement)

    def get_title(self):
        return self._gf('title')

    def set_title(self, title):
        """ @rtype: L{OptionName} """
        assert isinstance(title, unicode), 'title should be unicode'
        return self._sf('title', title)

    def get_position(self):
        return int(self._gf('position'))

    def set_position(self, position):
        """ @rtype: L{OptionName} """
        assert isinstance(position, int)
        return self._sf('position', int(position))

    @classmethod
    def new_option_name(cls):
        root = ElementTree.Element('option-name')
        tree = ElementTree.ElementTree(root)
        return OptionName(tree)
