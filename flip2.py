import nltk
import ast
import re
from nltk.corpus import state_union
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import wordnet
from nltk.corpus import sentiwordnet
import sentiment_mod as s

def tokenizeReviews(inputFileStr,outputFileStr):
    tokenizedReviews={}
    c = 0
    # train_text = state_union.raw("2006-GWBush.txt")
    inputFile = open(inputFileStr,"r").read()
    # inputFile = re.sub('\.*\n','.',inputFile)
    #tokenizer = PunktSentenceTokenizer(train_text)
    print ("Analysing reviews...")
    for sentence in sent_tokenize(inputFile):      
      sentiment_value, confidence = s.sentiment(sentence)
      out = sentence, sentiment_value, confidence
      print(sentence, sentiment_value, confidence)
      if confidence*100 == 100:
        if (c!=0):
          output = open(outputFileStr,"a")
        else:
          output = open(outputFileStr,"w")
          c = 1
        output.write(sentiment_value)
        output.write('\n')
        output.close()

