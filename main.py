from functions.speech_to_text import microphone
from functions.text_to_speech import speech
from functions.text_analyze import tokenize_no_stopword, stem, lemmatize

# text = "Accendi la luce della camera di Marco. Ieri sono andato all'ospedale"
while True:
    text = None

    while True:
        t = microphone()
        if t is not None:
            text = t
            break
    # speech(text)
    print('[*] t: ', text)
    # tokens = tokenize_no_stopword(text)
    # print('[*] T: ', tokens)
    # stokens = stem(tokens)
    # print('[*] S:', stokens)

    lem = lemmatize(text)
    print('\n[*] L:', lem)
    tokens = tokenize_no_stopword(lem)
    print('[*] T: ', tokens)
    if text == 'Ok Google Chiudi tutto':
        break
    elif all([x in ['ciao', 'computer', 'stare'] for x in tokens]):
        speech('Ciao a te!')


print(tokenize_no_stopword(lemmatize(text='Spegni tutte le luci. Accendi la luce in camera di Marco. Spegni la luce in camera di Marco')))