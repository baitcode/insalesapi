from array import array
import decimal
from xml.etree import ElementTree
from xml.etree.ElementTree import Element

class ApiObject(object):

    def get_id(self):
        try:
            return int(self._gf('id'))
        except ValueError:
            return -1

    def set_id(self, id):
        """@rtype:L{ApiObject}"""
        return self._sf('id', int(id))

    def get_created_at(self):
        #TODO: Test and fix
        return self._gf('created-at')

    def get_updated_at(self):
        #TODO: Test and fix
        return self._gf('updated-at')

    def _gf(self, name):
        obj = self.root().find(name)
        if obj is None:
            return ""
        return obj.text

    def _sf(self, name, value):
        """@rtype: L{ApiObject}"""
        value_type = dict()
        if isinstance(value, int):
            value_type['type'] = 'integer'
        elif isinstance(value, bool):
            value_type['type'] = 'boolean'
        elif isinstance(value, decimal.Decimal):
            value_type['type'] = 'decimal'
        elif isinstance(value, (list, array, dict, set)):
            value_type['type'] = 'array'
        elif isinstance(value, ApiObject): #TODO: check for iterator?
            pass
        else:
            value_type['type'] = 'text'

        return self._chainExecution(lambda obj: obj._createField(name, value, value_type))

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

        if not isinstance(tmp, Element):
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

    def dump(self, margin='\n', obj=None):
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
