# -------------------------------------------------------------------
lang = ['Italian', 'it-IT']

# tokenizing and stop-word elimination
from nltk.corpus import stopwords
import nltk
import string


# Tokenizer/ stopwords, punctuations, apostrophes elimination
def tokenize_no_stopword(text):
    ftokens = [w.split("'") for w in nltk.word_tokenize(text, language=lang[0]) if
               not w in set(stopwords.words(lang[0])) and w not in string.punctuation]
    return [y for x in ftokens for y in x]


# -------------------------------------------------------------------
from nltk.stem import SnowballStemmer


def stem(tokens):
    return [SnowballStemmer(language=lang[0].lower()).stem(t) for t in tokens]


# -------------------------------------------------------------------


from functions.pymorphit_cls import PyMorphITCLS as Lemmatizer

lem = Lemmatizer()


def lemmatize(text):
    return lem.lemmatize_line(line=text.replace("'", ' '), mode='Q')
# -------------------------------------------------------------------
