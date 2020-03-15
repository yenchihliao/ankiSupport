# import Operation
import toml
from LinkOperation import LinkVoc
from SearchOperation import SearchVoc
from Loop2XDecorator import Loop2XDecorator

class UsageFactory():
    def __init__(self):
        pass
    def createVoc(self):
        f = open('Vocs.txt', 'r')
        self.words = toml.load(f)
        f.close()
        self.link = Loop2XDecorator(LinkVoc(self.words))
        self.search = Loop2XDecorator(SearchVoc(self.words))
        return self
