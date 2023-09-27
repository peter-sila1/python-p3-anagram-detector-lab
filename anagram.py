# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word=word


    def match(self, word_list):
        myList=[]
        my_words=[letter for letter in self.word]
        for word in word_list:
            each_word=[letter for letter in word]
            if sorted(my_words) == sorted(each_word):
                myList.append(word)
        return myList