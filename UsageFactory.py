# import Operation
import toml
import LinkOperation
import SearchOperation
import OperationDecorator

class UsageFactory():
    def __init__(self):
        pass
    def createVoc(self):
        f = open('Vocs.txt', 'r')
        self.words = toml.load(f)
        f.close()
        self.link = OperationDecorator.Loop2X(LinkOperation.LinkVoc(self.words))
        self.search = OperationDecorator.Loop2X(SearchOperation.SearchVoc(self.words))
        return self
