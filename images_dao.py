from insalesapi.base_dao import BaseDao
from insalesapi.objects.image import Image

class ImagesDao(BaseDao):
    def __init__(self, api_key, api_password, host):
        super(ImagesDao, self).__init__('image', api_key, api_password, host)

    def get_list(self, product_id, lang=None):
        """ @rtype: L{list} """
        images = self.read('/admin/products/%d/images.xml' % product_id, lang)
        return Image.wrapCollection(images)

    def get(self, product_id, image_id, lang=None):
        """ @rtype: L{list} """
        images = self.read('/admin/products/%d/images/%d.xml' % (product_id, image_id), lang)
        return Image.wrapCollection(images)

    def add(self, product_id, image, lang=None):
        images = self.create('/admin/products/%d/images.xml' % product_id, image, lang)
        return Image.wrapCollection(images)

    def edit(self, product_id, image_id, lang=None):
        """ @rtype: L{list} """
        images = self.update('/admin/products/%d/images/%d' % (product_id, image_id), lang)
        return Image.wrapCollection(images)

    def remove(self, product_id, image_id, lang=None):
        return self.delete('/admin/products/%d/images/%d' % (product_id, image_id), lang)