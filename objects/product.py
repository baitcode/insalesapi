from insalesapi.objects.option_name import OptionName
from insalesapi.objects.modification import Modification
from xml.etree import ElementTree
from insalesapi.objects.image import Image
from insalesapi.objects.api_object import ApiObject
from insalesapi.objects.property_attribute import PropertyAttribute

class Product(ApiObject):
    #TODO: variants and variants-attributes, should be handled internally
    def __init__(self, treeElement):
        super(Product, self).__init__(treeElement)
        self.if_available = lambda variant: variant.get_quantity() > 0
        self.options_field_name = 'options'
        self.property_field_name = 'properties-attributes'

    def _variants_node(self):
        variants = self.root().find('variants')
        if variants is None or len(variants) == 0:
            variants = ElementTree.SubElement(self.root(), 'variants', attrib={'type': 'array'})
        return variants

    def _variants_attributes(self):
        variants = self.root().find('variants-attributes')
        if variants is None:
            variants = ElementTree.SubElement(self.root(), 'variants-attributes', attrib={'type': 'array'})
        return variants

    def _properties_attributes(self):
        properties = self.root().find(self.property_field_name)
        if properties is None:
            properties = ElementTree.SubElement(self.root(), self.property_field_name, attrib={'type': 'array'})
        return properties

    def _option_names(self):
        variants = self.root().find(self.options_field_name)
        if variants is None:
            variants = ElementTree.SubElement(self.root(), self.options_field_name, attrib={'type': 'array'})
        return variants

    def get_title(self):
        return self._gf('title')

    def set_title(self, title):
        """@rtype: L{Product}"""
        return self._sf('title', title)

    def get_html_title(self,):
        return self._gf('html-title')

    def set_html_title(self, title):
        """@rtype: L{Product}"""
        return self._sf('html-title', title)

    def get_meta_keywords(self):
        return self._gf('meta-keywords')

    def set_meta_keywords(self, keywords):
        """@rtype: L{Product}"""
        return self._sf('meta-keywords', keywords)

    def get_meta_description(self):
        return self._gf('meta-description')

    def set_meta_description(self, desc):
        """@rtype: L{Product}"""
        return self._sf('meta-description', desc)

    def get_modifications(self, filter = lambda x: True):
        return Modification.wrapCollection(self.root().iterfind('variant'), filter)

    def get_available_modifications(self):
        return self.get_modifications(self.if_available)

    def add_modification(self, modification):
        """@rtype: L{Product}"""
        assert isinstance(modification, Modification), 'modification should be Modification object.'
        self._variants_attributes()
        return self._sf('variants-attributes', modification)

    #is it really needed?
    def remove_modification(self, id):
        """@rtype: L{Product}"""
        modifications = self.get_modifications(lambda x: x.get_id() == id)
        for modification in modifications:
            self.root().remove(modification.root())
        return self

    def get_images(self):
        return Image.wrapCollection(self.root().iterfind('image'))

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
        self._option_names()
        return self._sf(self.options_field_name, option)

    def add_property(self, property):
        """@rtype: L{Product}"""
        assert isinstance(property, PropertyAttribute), 'option should be Option object.'
        self._properties_attributes()
        return self._sf(self.property_field_name, property)

    @classmethod
    def new_product(cls):
        root = ElementTree.Element("product")
        tree = ElementTree.ElementTree(root)
        return Product(tree)