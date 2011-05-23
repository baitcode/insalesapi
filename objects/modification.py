from unicodedata import decimal
from xml.etree import ElementTree
from insalesapi.objects.api_object import ApiObject
from insalesapi.objects.option_value import OptionValue

class Modification(ApiObject):
    def __init__(self, treeElement):
        super(Modification, self).__init__(treeElement)
        self.option_values = ElementTree.SubElement(self.root(), 'option-values', attrib={'type': 'array'})

    def get_title(self):
        return self._gf('title')

    def set_title(self, title):
        """ @rtype : L{Modification} """
        return self._sf('title', title)

    def get_quantity(self):
        """ #rtype: L{Modification}"""
        return int(self._gf('quantity'))

    def set_quantity(self, quantity):
        """ @rtype : L{Modification} """
        return self._sf('quantity', int(quantity))

    def get_price(self):
        return decimal(self._gf('price'))

    def set_price(self, price):
        """@rtype: L{Modification}"""
        return self._sf('price', decimal(price))

    def set_cost_price(self, cost_price):
        """@rtype: L{Modification}"""
        return self._sf('cost-price', decimal(cost_price))

    def get_cost_price(self):
        """@rtype: L{Modification}"""
        return decimal(self._gf('cost-price'))

    def set_old_price(self, old_price):
        """@rtype: L{Modification}"""
        return self._sf('old-price', decimal(old_price))

    def get_old_price(self):
        """@rtype: L{Modification}"""
        return decimal(self._gf('old-price'))

    def get_quantity(self):
        """@rtype: L{Modification}"""
        return int(self._gf('quantity'))

    def set_quantity(self, quantity):
        """@rtype: L{Modification}"""
        return self._sf('quantity', int(quantity))

    def get_options(self, filter = lambda x: True):
        return OptionValue.wrapCollection(self.root().findall('option-values'), filter)

    def add_option(self, option):
        """#rtype: L{Modification}"""
        return self._sf('option-values', option)

    def remove_option(self, id):
        """#rtype: L{Modification}"""
        options = self.get_options(lambda x: x.get_id() == id)
        for option in options:
            self.root().remove(option.root())
        return self

    def get_sku(self):
        return self._gf('sku')

    def set_sku(self, sku):
        """#rtype: L{Modification}"""
        return self._sf('sku', sku)

    @classmethod
    def new_modification(cls):
        root = ElementTree.Element('variant')
        tree = ElementTree.ElementTree(root)
        return Modification(tree)
