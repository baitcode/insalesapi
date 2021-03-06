from insalesapi.base_dao import BaseDao
from insalesapi.objects.product import Product

class ProductsDao(BaseDao):

    def __init__(self, api_key, api_password, host):
        super(ProductsDao, self).__init__('product', api_key, api_password, host)

    def get(self, product_id, lang=None):
        products = self.read('/admin/products/%d.xml' % product_id, lang)
        return Product.wrapCollection(products)

    def get_list(self, lang=None):
        products = self.read('/admin/products.xml', lang)
        return Product.wrapCollection(products)

    def add(self, product, lang=None):
        products = self.create('/admin/products.xml', product, lang)
        return Product.wrapCollection(products)
