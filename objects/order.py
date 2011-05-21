from insalesapi.objects.apiObject import ApiObject

class Order(ApiObject):
    def __init__(self, treeElement):
        super(Order, self).__init__(treeElement)
