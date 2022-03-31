import requests
import nltk
from nltk.tokenize import word_tokenize
import chunk


from nltk import util
from bs4 import BeautifulSoup
sampletxt = """this is very usefull book for study and explore"""
word_tokenize(sampletxt)
print(word_tokenize(sampletxt))

new = nltk.tokenize
chunking = new.sent_tokenize
def word_tokenize(text: sampletxt,
                  language: sampletxt = "english",
                  preserve_line: bool = False) -> list[sampletxt]:

                   print(chunking)

#data =requests.get((':', {'<DD>?<VB>*<JJ>'}))

#text = new_data.parser(':', {'<DD>?<VB>*<JJ>'})
#print(text)




