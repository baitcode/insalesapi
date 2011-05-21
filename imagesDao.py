from insalesapi.baseDao import BaseDao
from insalesapi.objects.image import Image

class ImagesDao(BaseDao):
    def __init__(self, api_key, api_password, host):
        super(ImagesDao, self).__init__('image', api_key, api_password, host)

    def getImages(self, product_id, lang=None):
        """
        @rtype: L{list}
        """
        images = self.read('/admin/products/%d/images.xml' % product_id, lang)
        return Image.wrapCollection(images)

    def getImage(self, product_id, image_id, lang=None):
        """
        @rtype: L{list}
        """
        images = self.read('/admin/products/%d/images/%d.xml' % (product_id, image_id), lang)
        return Image.wrapCollection(images)

    def addImage(self, product_id, image, lang=None):
        #TODO: validation, src title
        images = self.createFile('/admin/products/%d/images.xml' % product_id, image, lang)
        return Image.wrapCollection(images)

    def editImage(self, product_id, image_id, lang=None):
        """
        @rtype: L{list}
        """
        images = self.update('/admin/products/%d/images/%d' % (product_id, image_id), lang)
        return Image.wrapCollection(images)

    def removeImage(self, product_id, image_id, lang=None):
        return self.delete('/admin/products/%d/images/%d' % (product_id, image_id), lang)