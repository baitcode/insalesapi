import base64
from xml.etree import ElementTree
from insalesapi.objects.api_object import ApiObject

class Image(ApiObject):
    def __init__(self, treeElement):
        super(Image, self).__init__(treeElement)

    def set_title(self, title):
        """
        @rtype: L{Image}
        """
        assert isinstance(title, unicode), 'You''ve forgot to encode string title'
        return self._sf('title', title)

    def get_title(self):
        return self._gf('title')

    def set_filename(self, filename):
        """
        @rtype: L{Image}
        """
        assert isinstance(filename, unicode), 'You''ve forgot to encode string filename'
        return self._sf('filename', filename)

    def get_filename(self):
        return self._gf('filename')

    def set_attachment(self, file_path):
        """
        @rtype: L{Image}
        """
        file_reader = open(file_path)
        return self._sf('attachment', base64.b64encode(file_reader.read()))

    def get_attachment(self):
        return self._gf('attachment')

    def set_src(self, image_url):
        """
        @rtype: L{Image}
        """
        return self._sf('src', image_url)

    def get_src(self):
        return self._gf('src')

    def set_position(self, position):
        """
        @rtype: L{Image}
        """
        assert isinstance(position, int), "Position should positive integer number"
        return self._sf('position', int(position))

    def get_position(self):
        return int(self._gf('position'))

    def get_product_id(self):
        return int(self._gf('product-id'))

    def set_product_id(self, product_id):
        """
        @rtype: L{Image}
        """
        assert isinstance(product_id, int), "Position should positive integer number"
        return self._sf('product-id', int(product_id))

    def get_original_url(self):
        return self._gf('original-url')

    @classmethod
    def new_image(cls):
        root = ElementTree.Element('image')
        tree = ElementTree.ElementTree(root)
        return Image(tree)
