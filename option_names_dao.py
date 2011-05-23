from insalesapi.base_dao import BaseDao
from insalesapi.objects.option_name import OptionName

class OptionNamesDao(BaseDao):

    def __init__(self, api_key, api_password, host):
        super(OptionNamesDao, self).__init__('option-name', api_key, api_password, host)

    def get_list(self, lang=None):
        options = self.read('/admin/option_names.xml', lang)
        return OptionName.wrapCollection(options)

    def get(self, id, lang=None):
        options = self.read('/admin/option_names/%d' % id, lang)
        return OptionName.wrapCollection(options)

    def add(self, optionName, lang=None):
        options = self.create('/admin/option_names.xml', optionName, lang)
        return OptionName.wrapCollection(options)

    def edit(self, optionName, lang=None):
        id = optionName.get_Id()
        options = self.update('/admin/option_names/%d' % id, optionName, lang)
        return OptionName.wrapCollection(options)

    def remove(self, id, lang=None):
        return self.delete('/admin/option_names/%d' % id, lang)

