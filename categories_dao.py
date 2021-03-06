from insalesapi.base_dao import BaseDao
from insalesapi.objects.category import Category

class CategoriesDao(BaseDao):

    def __init__(self, api_key, api_password, host):
        super(CategoriesDao, self).__init__('category', api_key, api_password, host)

    def get_list(self, lang=None):
        """@rtype: L{list}"""
        categories = self.read('/admin/categories.xml', lang)
        return Category.wrapCollection(categories)

    def get(self, id, lang=None):
        """@rtype: L{list}"""
        categories = self.read('/admin/categories/%d' % id, lang)
        return Category.wrapCollection(categories)

    def edit(self, category, lang=None):
        """@rtype: L{list}"""
        categories = self.update('/admin/categories/%d' % int(category.get_id()), category, lang)
        return Category.wrapCollection(categories)

    def add(self, category, lang=None):
        categories = self.create('/admin/categories.xml', category, lang)
        return Category.wrapCollection(categories)

    def remove(self, id, lang=None):
        return self.delete('/admin/categories/%d' % id, lang)
