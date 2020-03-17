from Operation import Operation

class SearchVoc(Operation):
    def __init__(self, words):
        self.words = words
        self.helpMsg = "<word>"
        self.prefix = "search: "
    # Print all the linked entry of w
    def do(self, w):
        w = w[0]
        if w in self.words.keys():
            for ww in self.words[w]['links']:
                print(self.words[ww])
            return True
        else:
            return False
