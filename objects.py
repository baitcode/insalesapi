# -*- coding: utf-8 -*-
__author__ = 'bait'

from xml.etree import ElementTree

class ApiObject(object):

    def getId(self):
        return int(self.gf('id'))

    def gf(self, name):
        obj = self.root().find(name)
        if obj is None:
            return ""
        return obj.text

    def __init__(self, treeElement):
        super(ApiObject, self).__init__()
        self.element = treeElement

    def root(self):
        """
        @rtype: L{xml.etree.ElementTree.Element}
        """
        return self.element.getroot()

    @classmethod
    def wrapCollection(cls, elements, custom_filter = lambda x: True):
        return filter(custom_filter, (cls(ElementTree.ElementTree(el)) for el in elements))

    def _prepare_element(self, attributes, name, root):
        tmp = root.find(name)
        if tmp is None:
            tmp = ElementTree.SubElement(root, name)
        for k, v in attributes.items():
            tmp.set(k, v)
        return tmp

    def _createFieldForRoot(self, root, name, value, attributes = dict(), ignore_encoding=False):
        elementIsArray = lambda el: el.attrib.has_key('type') and el.attrib['type']=='array'
        tmp = self._prepare_element(attributes, name, root)
        if not isinstance(value, ApiObject):
            if ignore_encoding:
                tmp.text = value
            else:
                tmp.text = unicode(value)
        elif elementIsArray(tmp):
            tmp.append(value.element.getroot())

    def _createField(self, name, value, attributes = dict(), ignore_encoding=False):
        self._createFieldForRoot(self.root(), name, value, attributes, ignore_encoding)

    def _chainExecution(self, x = lambda x: x):
        x(self)
        return self

    def dump(self, margin='', obj=None):
        if obj is None:
            obj = self

        for method in {m for m in dir(obj) if m.startswith('get')}:
            field = self.__getattribute__(method)()
            if isinstance(field, list):
                print "{0}{1:15}".format(margin+'\t', method[3:])
                for field_element in field:
                    if isinstance(field_element, ApiObject):
                        field_element.dump(margin+'\t\t')
                    else:
                        print "{0}{1:15} : {2:15}".format(margin+'\t\t', method[3:], unicode(field_element).encode('utf-8'))
            else:
                print "{0}{1:15} : {2:15}".format(margin, method[3:], unicode(field).encode('utf-8'))
        if margin=='':
            print ''

    def __str__(self):
        return '<?xml version="1.0" encoding="UTF-8"?>'+ElementTree.tostring(self.root(), encoding='utf-8')

class Image(ApiObject):
    def __init__(self, treeElement):
        super(Image, self).__init__(treeElement)

    def setTitle(self, title):
        """
        @rtype: L{Image}
        """
        assert isinstance(title, unicode), 'You''ve forgot to encode string title'
        return self._chainExecution(lambda image: image._createField('title', title))

    def setFilename(self, filename):
        """
        @rtype: L{Image}
        """
        assert isinstance(filename, unicode), 'You''ve forgot to encode string filename'
        return self._chainExecution(lambda image: image._createField('filename', filename))

    def setAttachment(self, file_content):
        """
        @rtype: L{Image}
        """
        return self._chainExecution(lambda image: image._createField('attachment', file_content))

    def setSrc(self, image_url):
        """
        @rtype: L{Image}
        """
        return self._chainExecution(lambda image: image._createField('src', image_url))

    def setPosition(self, position):
        """
        @rtype: L{Image}
        """
        assert isinstance(position, int), "Position should positive integer number"
        return self._chainExecution(lambda image: image._createField('position', position, dict(type='integer')))

    def setProductId(self, product_id):
        """
        @rtype: L{Image}
        """
        assert isinstance(product_id, int), "Position should positive integer number"
        return self._chainExecution(lambda image: image._createField('product-id', product_id, dict(type='integer')))

    def getTitle(self):
        return self.gf('title')

    def getProductId(self):
        return int(self.gf('product-id'))

    def getPosition(self):
        return int(self.gf('position'))

    def getAttachment(self):
        return self.gf('attachment')

    def getFilename(self):
        return self.gf('filename')

    def getOriginalUrl(self):
        return self.gf('original-url')

    def __str__(self):
        title = self.gf('title')
        src = self.gf('src')
        filename = self.gf('filename')
        attachment = self.gf('attachment')
        position = self.gf('position')
        output = '<?xml version="1.0" encoding="UTF-8"?><image>'
        params = ()
        if title != '':
            output += '<title>%s</title>'
            params += tuple([title])

        if position != '':
            output += '<position type="integer">%d</position>'
            params += tuple([position])
            
        if filename != '':
            output += '<filename>%s</filename>'
            params += tuple([filename])

        if attachment != '':
            output += '<attachment>%s</attachment>'
            params += tuple([attachment])

        if src != '':
            output += '<src>%s</src>'
            params += tuple([src])
        output += '</image>'

        return (output % params).encode('utf-8')


    @classmethod
    def newImage(cls):
        root = ElementTree.Element('image')
        tree = ElementTree.ElementTree(root)
        return Image(tree)

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

class Category(ApiObject):
    def __init__(self, treeElement):
        super(Category, self).__init__(treeElement)

    def getParentId(self):
        return int(self.gf('id'))

    def getTitle(self):
        return self.gf('title')

    def getPosition(self):
        return int(self.gf('position'))

    def setParent(self, parent_id):
        """@rtype: L{Category}"""
        return self._chainExecution(lambda category: category._createField('parent-id', parent_id, dict(type='integer')))

    def setTitle(self, title):
        """@rtype: L{skychip.insales.objects.Category}"""
        return self._chainExecution(lambda category: category._createField('title', title))

    def setPosition(self, position):
        """@rtype: L{skychip.insales.objects.Category}"""
        return self._chainExecution(lambda category: category._createField('position', position, dict(type='integer')))

    @classmethod
    def newCategory(cls):
        """
        @rtype: L{Category}
        """
        root = ElementTree.Element("category")
        tree = ElementTree.ElementTree(root)
        return Category(tree)

