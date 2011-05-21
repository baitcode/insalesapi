from insalesapi.objects.api_object import ApiObject

class Order(ApiObject):
    def __init__(self, treeElement):
        super(Order, self).__init__(treeElement)
