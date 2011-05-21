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
