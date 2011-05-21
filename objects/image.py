from xml.etree import ElementTree
from insalesapi.objects.apiObject import ApiObject

class Image(ApiObject):
    def __init__(self, treeElement):
        super(Image, self).__init__(treeElement)

    def setTitle(self, title):
        """
        @rtype: L{Image}
        """
        assert isinstance(title, unicode), 'You''ve forgot to encode string title'
        return self.sf('title', title)

    def getTitle(self):
        return self.gf('title')

    def setFilename(self, filename):
        """
        @rtype: L{Image}
        """
        assert isinstance(filename, unicode), 'You''ve forgot to encode string filename'
        return self.sf('filename', filename)

    def getFilename(self):
        return self.gf('filename')

    def setAttachment(self, file_content):
        """
        @rtype: L{Image}
        """
        return self.sf('attachment', file_content)

    def getAttachment(self):
        return self.gf('attachment')

    def setSrc(self, image_url):
        """
        @rtype: L{Image}
        """
        return self.sf('src', image_url)

    def getSrc(self):
        return self.gf('src')

    def setPosition(self, position):
        """
        @rtype: L{Image}
        """
        assert isinstance(position, int), "Position should positive integer number"
        return self.sf('position', int(position))

    def getPosition(self):
        return int(self.gf('position'))

    def getProductId(self):
        return int(self.gf('product-id'))

    def setProductId(self, product_id):
        """
        @rtype: L{Image}
        """
        assert isinstance(product_id, int), "Position should positive integer number"
        return self.sf('product-id', int(product_id))

    def getOriginalUrl(self):
        return self.gf('original-url')

    @classmethod
    def newImage(cls):
        root = ElementTree.Element('image')
        tree = ElementTree.ElementTree(root)
        return Image(tree)

#
#    def __str__(self):
#        title = self.gf('title')
#        src = self.gf('src')
#        filename = self.gf('filename')
#        attachment = self.gf('attachment')
#        position = self.gf('position')
#        output = '<?xml version="1.0" encoding="UTF-8"?><image>'
#        params = ()
#        if title != '':
#            output += '<title>%s</title>'
#            params += tuple([title])
#
#        if position != '':
#            output += '<position type="integer">%d</position>'
#            params += tuple([position])
#
#        if filename != '':
#            output += '<filename>%s</filename>'
#            params += tuple([filename])
#
#        if attachment != '':
#            output += '<attachment>%s</attachment>'
#            params += tuple([attachment])
#
#        if src != '':
#            output += '<src>%s</src>'
#            params += tuple([src])
#        output += '</image>'
#
#        return (output % params).encode('utf-8')
