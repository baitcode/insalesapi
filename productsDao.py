from insalesapi.baseDao import BaseDao
from insalesapi.objects.product import Product

class ProductsDao(BaseDao):

    def __init__(self, api_key, api_password, host):
        super(ProductsDao, self).__init__('product', api_key, api_password, host)

    def getProductList(self, lang=None):
        products = self.read('/admin/products.xml', lang)
        return Product.wrapCollection(products)

    def addProduct(self, product, lang=None):
        products = self.create('/admin/products.xml', product, lang)
        return Product.wrapCollection(products)
