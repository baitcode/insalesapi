from unicodedata import decimal
from xml.etree import ElementTree
from insalesapi.objects.api_object import ApiObject
from insalesapi.objects.option_value import OptionValue

class Modification(ApiObject):
    def __init__(self, treeElement):
        super(Modification, self).__init__(treeElement)
        self.option_values = ElementTree.SubElement(self.root(), 'option-values', attrib={'type': 'array'})

    def getTitle(self):
        return self.gf('title')

    def setTitle(self, title):
        """ @rtype : L{Modification} """
        return self.sf('title', title)

    def getQuantity(self):
        """ #rtype: L{Modification}"""
        return int(self.gf('quantity'))

    def setQuantity(self, quantity):
        """ @rtype : L{Modification} """
        return self.sf('quantity', int(quantity))

    def getPrice(self):
        return decimal(self.gf('price'))

    def setPrice(self, price):
        """@rtype: L{Modification}"""
        return self.sf('price', decimal(price))

    def setCostPrice(self, cost_price):
        """@rtype: L{Modification}"""
        return self.sf('cost-price', decimal(cost_price))

    def getCostPrice(self):
        """@rtype: L{Modification}"""
        return decimal(self.gf('cost-price'))

    def setOldPrice(self, old_price):
        """@rtype: L{Modification}"""
        return self.sf('old-price', decimal(old_price))

    def getOldPrice(self):
        """@rtype: L{Modification}"""
        return decimal(self.gf('old-price'))

    def getQuantity(self):
        """@rtype: L{Modification}"""
        return int(self.gf('quantity'))

    def setQuantity(self, quantity):
        """@rtype: L{Modification}"""
        return self.sf('quantity', int(quantity))

    def getOptions(self, filter = lambda x: True):
        return OptionValue.wrapCollection(self.root().findall('option-values'), filter)

    def addOption(self, option):
        """#rtype: L{Modification}"""
        return self.sf('option-values', option)

    def removeOption(self, id):
        """#rtype: L{Modification}"""
        options = self.getOptions(lambda x: x.getId() == id)
        for option in options:
            self.root().remove(option.root())
        return self

    def getSku(self):
        return self.gf('sku')

    def setSku(self, sku):
        """#rtype: L{Modification}"""
        return self.sf('sku', sku)

    @classmethod
    def newModification(cls):
        root = ElementTree.Element('variant')
        tree = ElementTree.ElementTree(root)
        return Modification(tree)
