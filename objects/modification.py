class Modification(ApiObject):
    def __init__(self, treeElement):
        super(Modification, self).__init__(treeElement)
        self.option_values = ElementTree.SubElement(self.root(), 'option-values', attrib={'type': 'array'})

    def getName(self):
        return self.element.find('title').text

    def getQuantity(self):
        return int(self.element.find('quantity').text)

    @classmethod
    def newModification(cls):
        root = ElementTree.Element('variant')
        tree = ElementTree.ElementTree(root)
        return Modification(tree)

    def setPrice(self, price):
        """@rtype: L{Modification}"""
        return self._chainExecution(lambda modification: modification._createField('price', price, attributes=dict(type='decimal')))

    def addOption(self, option):
        return self._chainExecution(lambda modification: modification._createField('option-values', option))