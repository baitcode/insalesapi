import urlparse
from xml.etree.ElementTree import dump
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

    def edit(self, product_id, image_id, image, lang=None):
        """ @rtype: L{list} """
        images = self.update('/admin/products/%d/images/%d' % (product_id, image_id), image, lang)
        return Image.wrapCollection(images)

    def remove(self, product_id, image_id, lang=None):
        return self.delete('/admin/products/%d/images/%d' % (product_id, image_id), lang)

    def image_exists(self, images, filename):
        exists = False
        for image in images:
            server_filename = urlparse.urlparse(image.get_original_url()).path.rpartition('/')[2]
            if server_filename == filename:
                exists = True
        return exists

    def _reserve_image_position(self, position, product_id, product_images):
        rang = range(position, len(product_images) + 1)
        rang.reverse()
        for i in rang:
            img = Image.new_image().set_position(i + 1)
            id = product_images[i - 1].get_id()
            self.edit(product_id, id, img)

    def insert_image(self, product_id, image, position):
        product_images = self.get_list(product_id)

        if self.image_exists(product_images, image.get_filename()):
            return

        if position < 0:
            position = len(product_images) + 1 + position

        self._reserve_image_position(position, product_id, product_images)
        uploaded_image = self.add(product_id, image)[0]
        uploaded_image.set_position(position)
        self.edit(product_id, uploaded_image.get_id(), uploaded_image)

