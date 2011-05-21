from insalesapi.objects.apiObject import ApiObject
from xml.etree import ElementTree

class Option(ApiObject):
    def __init__(self, treeElement):
        super(Option, self).__init__(treeElement)

    def setId(self, id):
        """
        @rtype: L{Option}
        """
        assert isinstance(id, int), 'Value should be int'
        return self._chainExecution(lambda option: option._createField('option-name-id', id, dict(type='integer')))

    def setTitle(self, title):
        """
        @rtype: L{Option}
        """
        assert isinstance(title, unicode), 'title should be unicode'
        return self._chainExecution(lambda option: option._createField('title', title))

    def setPosition(self, position):
        """
        @rtype: L{Option}
        """
        assert isinstance(position, int)
        return self._chainExecution(lambda option: option._createField('position', position))

    def setOptionNameId(self, option_name_id):
        """
        @rtype: L{Option}
        """
        assert isinstance(option_name_id, unicode), 'option_name_id should be unicode'
        return self._chainExecution(lambda option: option._createField('option_name_id', option_name_id))

    @classmethod
    def newOptionValue(cls):
        root = ElementTree.Element('option-value')
        tree = ElementTree.ElementTree(root)
        return Option(tree)

    @classmethod
    def newOptionName(cls):
        root = ElementTree.Element('option-name')
        tree = ElementTree.ElementTree(root)
        return Option(tree)
