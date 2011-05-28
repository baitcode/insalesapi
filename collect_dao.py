from insalesapi.base_dao import BaseDao
from insalesapi.objects.collect import Collect

class CollectDao(BaseDao):
    def __init__(self, api_key, api_password, host):
        super(CollectDao, self).__init__('collect', api_key, api_password, host)

    def add(self, collection_id, product_id, lang=None):
        collect = Collect.newCollect()\
            .set_collection_id(collection_id)\
            .set_product_id(product_id)
        collections = self.create('/admin/collect.xml', collect, lang)
        return Collect.wrapCollection(collections)
