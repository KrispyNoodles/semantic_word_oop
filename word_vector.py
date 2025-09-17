import gensim.downloader as api
from nltk.stem import PorterStemmer

class WordVector():    

    # loading the model, the model will be downloaded the first time
    MODEL = api.load("glove-twitter-200")

    # excluding stems that were present before
    EXCLUDED_STEMS = []

    def __init__(self, text, vector=None):

        # initailising the text and vector
        self.text = text
        
        # if a vector isnt sent then it will be created
        if vector is None:        
            self.vector = WordVector.MODEL.get_vector(text)

        else:
            self.vector = vector
        
        # creating a list of stem words that is it not possible to recover back into 
        WordVector.EXCLUDED_STEMS.append(PorterStemmer().stem(text))

    # generates the word
    def word_generator(self, new_vector):

        # retrieve the word
        # write a function which excludes the stem itself
        # if the entire list of results contains the stems of both the self and other words, it will result in an empty list causing an error
        result = WordVector.MODEL.most_similar([new_vector], topn=8)

        final_result = []

        # ignoring the similarity score and using the words only
        for word, _ in result:

            if PorterStemmer().stem(word) not in WordVector.EXCLUDED_STEMS:
                
                # final list exlcuding the words being used
                final_result.append(word)

        # return an instance of the word to be further manipulated with if neccessary 
        return WordVector(final_result[0], new_vector)

    # addition function
    def __add__(self, other):

        new_vector = self.vector + other.vector
        return WordVector.word_generator(self, new_vector)
    
    # subtraction
    def __sub__(self, other):

        new_vector = self.vector - other.vector
        return WordVector.word_generator(self, new_vector)

    # printing the text 
    def __repr__(self):
        return self.text

    # creating a class method to change the model being used
    @classmethod
    def update_model(cls, model_name):
        WordVector.MODEL = api.load(model_name)