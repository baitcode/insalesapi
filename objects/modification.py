from decimal import Decimal
from unicodedata import decimal
from xml.etree import ElementTree
from insalesapi.objects.api_object import ApiObject
from insalesapi.objects.option_value import OptionValue

class Modification(ApiObject):
    def __init__(self, treeElement):
        super(Modification, self).__init__(treeElement)

    def _options_node(self):
        options = self.root().find('options')
        if options is None or len(options) == 0:
            options = ElementTree.SubElement(self.root(), 'options', attrib={'type': 'array'})
        return options

    def _option_values_node(self):
        options = self.root().find('option-values')
        if options is None or len(options) == 0:
            options = ElementTree.SubElement(self.root(), 'option-values', attrib={'type': 'array'})
        return options

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
        try:
            return Decimal(self._gf('price'))
        except TypeError:
            return -1

    def set_price(self, price):
        """@rtype: L{Modification}"""
        return self._sf('price', Decimal(price))

    def set_cost_price(self, cost_price):
        """@rtype: L{Modification}"""
        return self._sf('cost-price', Decimal(cost_price))

    def get_cost_price(self):
        """@rtype: L{Modification}"""
        try:
            return Decimal(self._gf('cost-price'))
        except TypeError:
            return -1

    def set_old_price(self, old_price):
        """@rtype: L{Modification}"""
        return self._sf('old-price', Decimal(old_price))

    def get_old_price(self):
        """@rtype: L{Modification}"""
        try:
            return Decimal(self._gf('old-price'))
        except TypeError:
            return -1

    def get_quantity(self):
        """@rtype: L{Modification}"""
        return int(self._gf('quantity'))

    def set_quantity(self, quantity):
        """@rtype: L{Modification}"""
        return self._sf('quantity', int(quantity))

    def get_options(self, filter = lambda x: True):
        node = self._option_values_node()
        return OptionValue.wrapCollection(node.findall('option-value'), filter)

    def get_new_options(self, filter = lambda x: True):
        node = self._options_node()
        return OptionValue.wrapCollection(node.findall('option'), filter)

    def add_option(self, option):
        """#rtype: L{Modification}"""
        self._options_node()
        return self._sf('options', option)

    def remove_option(self, id):
        """#rtype: L{Modification}"""
        options = self.get_options(lambda x: x.get_id() == id)
        for option in options:
            self.root().remove(option.root())
        return self

    def get_sku(self):
        return self._gf('sku')

    def set_sku(self, sku):
        """@rtype: L{Modification}"""
        return self._sf('sku', sku)

    @classmethod
    def new_modification(cls):
        root = ElementTree.Element('variant')
        tree = ElementTree.ElementTree(root)
        return Modification(tree)
