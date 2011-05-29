from insalesapi.objects.api_object import ApiObject
from xml.etree import ElementTree

class OptionValue(ApiObject):
    def __init__(self, treeElement):
        super(OptionValue, self).__init__(treeElement)

    def get_value(self):
        return self._gf('value')

    def get_value(self, title):
        """ @rtype: L{OptionValue} """
        assert isinstance(title, unicode), 'title should be unicode'
        return self._sf('value', title)

    def get_position(self):
        try:
            return int(self._gf('position'))
        except ValueError:
            return -1

    def set_position(self, position):
        """ @rtype: L{OptionValue} """
        assert isinstance(position, int)
        return self._sf('position', int(position))

    def get_option_name_id(self):
        try:
            return int(self._gf('option-name-id'))
        except ValueError:
            return -1

    def set_option_name_id(self, option_name_id):
        """ @rtype: L{OptionValue} """
        return self._sf('option-name-id', int(option_name_id))

    @classmethod
    def new_option_value(cls):
        root = ElementTree.Element('option')
        tree = ElementTree.ElementTree(root)
        return OptionValue(tree)
