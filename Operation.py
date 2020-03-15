import toml

class Operation():
    def __init__(self, words):
        self.helpMsg = "link, search"
        self.prefix = "Abstract operation"
        pass
    def do(self):
        pass
    def printHelp(self):
        print(self.helpMsg)
        # f = open('Vocs.txt', 'r')
        # self.words = toml.load(f)
    # list all the word that has no links
    # def list(self, w='*'):
    #     NotFound = True
    #     for k in self.words.keys():
    #         if len(self.words[k]['links']) == 0:
    #             NotFound = False
    #             print(k)
    #     if NotFound:
    #         print("Every word is linked.")
