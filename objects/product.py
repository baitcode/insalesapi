from insalesapi.objects.option import Option
from insalesapi.objects.modification import Modification
from xml.etree import ElementTree
from insalesapi.objects.image import Image
from insalesapi.objects.apiObject import ApiObject

class Product(ApiObject):
    def __init__(self, treeElement):
        super(Product, self).__init__(treeElement)
        self.if_available = lambda variant: variant.getQuantity() > 0
        self.modifications = ElementTree.SubElement(self.root(), 'variants', attrib={'type': 'array'})
        self.option_names = ElementTree.SubElement(self.root(), 'option-names', attrib={'type': 'array'})

    def getName(self):
        return self.element.find('title').text

    def getSizes(self, custom_filter = lambda tmp: True):
        variants = self.element.find('variants').findall('variant')
        return Modification.wrapCollection(variants, custom_filter)

    def getAvailableSizes(self):
        return self.getSizes(self.if_available)

    def getImages(self):
        images = self.element.find('images').findall('image')
        return Image.wrapCollection(images)

    @classmethod
    def newProduct(cls):
        root = ElementTree.Element("product")
        tree = ElementTree.ElementTree(root)
        return Product(tree)

    def setCategory(self, category_id):
        """@rtype: L{Product}"""
        return self._chainExecution(lambda product: product._createField('category-id', category_id, attributes=dict(type='integer')))

    def setTitle(self, title):
        """@rtype: L{Product}"""
        return self._chainExecution(lambda product: product._createField('title', title))

    def setDescription(self, description):
        """@rtype: L{Product}"""
        return self._chainExecution(lambda product: product._createField('description', description))

    def setShortDescription(self, description):
        """@rtype: L{Product}"""
        return self._chainExecution(lambda product: product._createField('short-description', description))

    def addModification(self, modification):
        """@rtype: L{Product}"""
        assert isinstance(modification, Modification), 'modification should be Modification object.'
        return self._chainExecution(lambda product: product._createField('variants', modification))

    def addOptionName(self, option):
        """@rtype: L{Product}"""
        assert isinstance(option, Option), 'option should be Option object.'
        return self._chainExecution(lambda product: product._createField('option-names', option))
