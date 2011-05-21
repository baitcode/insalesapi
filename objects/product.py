from insalesapi.objects.option_name import OptionName
from insalesapi.objects.modification import Modification
from xml.etree import ElementTree
from insalesapi.objects.image import Image
from insalesapi.objects.api_object import ApiObject

class Product(ApiObject):
    def __init__(self, treeElement):
        super(Product, self).__init__(treeElement)
        self.if_available = lambda variant: variant.getQuantity() > 0
        self.modifications = ElementTree.SubElement(self.root(), 'variants', attrib={'type': 'array'})
        self.option_names = ElementTree.SubElement(self.root(), 'option-names', attrib={'type': 'array'})

    def getTitle(self):
        return self.gf('title')

    def setTitle(self, title):
        """@rtype: L{Product}"""
        return self.sf('title', title)

    def getModifications(self, filter = lambda x: True):
        return Modification.wrapCollection(self.root().findall('variant'), filter)

    def getAvailableModifications(self):
        return self.getModifications(self.if_available)

    def addModification(self, modification):
        """@rtype: L{Product}"""
        assert isinstance(modification, Modification), 'modification should be Modification object.'
        return self.sf('variants', modification)

    #is it really needed?
    def removeModification(self, id):
        """@rtype: L{Product}"""
        modifications = self.getModifications(lambda x: x.getId() == id)
        for modification in modifications:
            self.root().remove(modification.root())
        return self

    def getImages(self):
        return Image.wrapCollection(self.root().findall('image'))

    def getCategory(self):
        """@rtype: L{Product}"""
        return int(self.gf('category-id'))

    def setCategory(self, category_id):
        """@rtype: L{Product}"""
        return self.sf('category-id', int(category_id))

    def getDescription(self):
        """@rtype: L{Product}"""
        return self.gf('description')

    def setDescription(self, description):
        """@rtype: L{Product}"""
        return self.sf('description', description)

    def getShortDescription(self):
        return self.gf('short-description')

    def setShortDescription(self, description):
        """@rtype: L{Product}"""
        return self.sf('short-description', description)

    def getOptionNames(self):
        return OptionName.wrapCollection(self.root().findall('option-name'))

    def addOptionName(self, option):
        """@rtype: L{Product}"""
        assert isinstance(option, OptionName), 'option should be Option object.'
        return self.sf('option-names', option)

    @classmethod
    def newProduct(cls):
        root = ElementTree.Element("product")
        tree = ElementTree.ElementTree(root)
        return Product(tree)