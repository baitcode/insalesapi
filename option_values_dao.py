from insalesapi.base_dao import BaseDao
from insalesapi.objects.option_value import OptionValue

class OptionValuesDao(BaseDao):

    def __init__(self, api_key, api_password, host):
        super(OptionValuesDao, self).__init__('option-value', api_key, api_password, host)

    def get_list(self, lang=None):
        options = self.read('/admin/option_values.xml', lang)
        return OptionValue.wrapCollection(options)

    def get_list_by_option_name(self, optionNameId, lang=None):
        options = self.read('/admin/option_names/%d/option_values.xml' % optionNameId, lang)
        return OptionValue.wrapCollection(options)

    def get(self, optionNameId, id, lang=None):
        options = self.read('/admin/option_names/%d/option_values/%d' % (optionNameId, id), lang)
        return OptionValue.wrapCollection(options)

    def edit(self, optionNameId, optionValue, lang=None):
        id = optionValue.get_id()
        options = self.update('/admin/option_names/%d/option_values/%d' % (optionNameId, id), optionValue, lang)
        return OptionValue.wrapCollection(options)

    def add(self, optionNameId, optionValue, lang=None):
        #TODO: check
        options = self.create('/admin/option_names/%d/option_values.xml' % optionNameId, optionValue, lang)
        return OptionValue.wrapCollection(options)

    def remove(self, optionNameId, id, lang=None):
        return self.delete('/admin/option_names/%d/option_values/%d' % (optionNameId, id), lang)

