from xml.etree import ElementTree
from insalesapi.objects.apiObject import ApiObject

class Collection(ApiObject):
    def __init__(self, treeElement):
        super(Collection, self).__init__(treeElement)

    def isHidden(self):
        return bool(self.gf('is-hidden'))

    def setIsHidden(self, hidden):
        return self.sf('is-hidden', bool(hidden))

    def getParentId(self):
        return int(self.gf('parent-id'))

    def setParentId(self, parentId):
        return self.sf('parent-id', parentId)


    def getToTorgMail(self):
        return bool(self.gf('to-torg-mail'))

    def setToTorgMail(self, val):
        return self.sf('to-torg-mail', bool(val))

    def getToYandexMarket(self):
        return bool(self.gf('to-yandex-market'))

    def setToYandexMarket(self, val):
        return self.sf('to-yandex-market', bool(val))

    def getTitle(self):
        return bool(self.gf('title'))

    def setTitle(self, title):
        return self.sf('title', title)

    def getDescription(self):
        return self.gf('description')

    def setDescritption(self, description):
        return self.sf('description', description)

    def getHtmlTitle(self):
        return self.gf('html-title')

    def setHtmlTitle(self, title):
        return self.sf('html-title', title)

    def getMetaDescription(self):
        return self.gf('meta-description')

    def setMetaDescription(self, description):
        return self.sf('meta-description', description)

    def getMetaKeywords(self):
        return self.gf('meta-keywords')

    def setMetaKeywords(self, keywords):
        return self.sf('meta-keywords', keywords)

    def getPermalink(self):
        return self.gf('permalink')

    def setPermalink(self, permalink):
        return self.sf('permalink', permalink)

    def getUrl(self):
        return self.gf('url')

    @classmethod
    def newCollection(cls):
        root = ElementTree.Element('collection')
        tree = ElementTree.ElementTree(root)
        return Collection(tree)