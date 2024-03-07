# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()


    def match(self, words):
        return [wrd for wrd in words if sorted(wrd.lower()) == sorted(self.word)]
    