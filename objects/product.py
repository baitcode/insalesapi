from insalesapi.objects.option_name import OptionName
from insalesapi.objects.modification import Modification
from xml.etree import ElementTree
from insalesapi.objects.image import Image
from insalesapi.objects.api_object import ApiObject

class Product(ApiObject):
    def __init__(self, treeElement):
        super(Product, self).__init__(treeElement)
        self.if_available = lambda variant: variant.get_quantity() > 0
        self.modifications = ElementTree.SubElement(self.root(), 'variants', attrib={'type': 'array'})
        self.option_names = ElementTree.SubElement(self.root(), 'option-names', attrib={'type': 'array'})

    def get_title(self):
        return self._gf('title')

    def set_title(self, title):
        """@rtype: L{Product}"""
        return self._sf('title', title)

    def get_modifications(self, filter = lambda x: True):
        return Modification.wrapCollection(self.root().findall('variant'), filter)

    def get_available_modifications(self):
        return self.get_modifications(self.if_available)

    def add_modification(self, modification):
        """@rtype: L{Product}"""
        assert isinstance(modification, Modification), 'modification should be Modification object.'
        return self._sf('variants', modification)

    #is it really needed?
    def remove_modification(self, id):
        """@rtype: L{Product}"""
        modifications = self.get_modifications(lambda x: x.get_Id() == id)
        for modification in modifications:
            self.root().remove(modification.root())
        return self

    def get_images(self):
        return Image.wrapCollection(self.root().findall('image'))

    def get_category(self):
        """@rtype: L{Product}"""
        return int(self._gf('category-id'))

    def set_category(self, category_id):
        """@rtype: L{Product}"""
        return self._sf('category-id', int(category_id))

    def get_description(self):
        """@rtype: L{Product}"""
        return self._gf('description')

    def set_description(self, description):
        """@rtype: L{Product}"""
        return self._sf('description', description)

    def get_short_description(self):
        return self._gf('short-description')

    def set_short_description(self, description):
        """@rtype: L{Product}"""
        return self._sf('short-description', description)

    def get_option_names(self):
        return OptionName.wrapCollection(self.root().findall('option-name'))

    def add_option_name(self, option):
        """@rtype: L{Product}"""
        assert isinstance(option, OptionName), 'option should be Option object.'
        return self._sf('option-names', option)

    @classmethod
    def new_product(cls):
        root = ElementTree.Element("product")
        tree = ElementTree.ElementTree(root)
        return Product(tree)