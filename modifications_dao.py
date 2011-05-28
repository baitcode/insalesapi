from insalesapi.base_dao import BaseDao
from insalesapi.objects.modification import Modification

class ModificationsDao(BaseDao):

    def __init__(self, api_key, api_password, host):
        super(ModificationsDao, self).__init__('variant', api_key, api_password, host)

    def get_list(self, product_id, lang=None):
        """@rtype: L{list}"""
        modifications = self.read('/admin/products/%d/variants.xml' % product_id, lang)
        return Modification.wrapCollection(modifications)

    def get(self, product_id, id, lang=None):
        """@rtype: L{list}"""
        modifications = self.read('/admin/products/%d/variants/%d' % (product_id, id), lang)
        return Modification.wrapCollection(modifications)

    def edit(self, product_id, modification, lang=None):
        """@rtype: L{list}"""
        modifications = self.update('/admin/products/%d/variants/%d' % (product_id, modification.get_id()), modification, lang)
        return Modification.wrapCollection(modifications)

    def add(self, product_id, modification, lang=None):
        modifications = self.create('/admin/products/%d/variants.xml' % product_id, modification, lang)
        return Modification.wrapCollection(modifications)

    def remove(self, product_id, id, lang=None):
        return self.delete('/admin/products/%d/variants/%d.xml' % (product_id, id), lang)
