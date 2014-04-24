#!/usr/bin/env python
import sys
import json
import string


## list of unmeaningful words
STOPWORDS = ['a','able','about','across','after','all','almost','also','am','among',
'an','and','any','are','as','at','be','because','been', 'being', 'but','by','can','name','makes','talking','looks','old',
'cannot','could','dear','did','do','does', 'anything','done','either','else','ever','every',
'for','from','get','got','had','has','have','he','her','hers','him','his','free','return',
'how','however','i','if','in','into','is','it','its','just','least','let','hate','week','time','life',
'like','likely','may','me','might','most','must','my','neither','no','nor','real','tomorrow',
'not','of','off','often','on','only','or','other','our','own','rather','said','girls','things',
'say','says','she','put','sure','already','very','should','since','so','some','than','that','the','their','day','year','today',
'them','then','there','these','they','this','tis','to','too','twas','us','best','shit','girl',
'wants','was','we','were','what','when','where','which','while','who','stop','give','world',
'whom','why','will','with','would','yet','you','your', 'http','https', 'www', 'more','much', 'fuck',
'here','one', 'back', 'see', 'saw', 'seen','dont', 'you', 'me' ,'via' ,'wanna', 'you\'re','it\'s',
'take', 'haha','yes','think', 'thing', 'doesn\'t','wait','you','gonna','come','man','i\'ve','keep','make','next',
'need','over','that\'s','never','wait','getting', 'now', 'can\'t', 'new' , 'don\'t', 'out', 'know',
'really','going','you\'ve','i\'m','live','gimme', 'still', 'well', 'even', 'i\'ll', 'ain\'t','didn\'t', 'made', 'way', 'want',
'please', 'first', 'right', 'wrong', 'thanks' ,'last', 'thank', 'win', 'happy','we\'ll', 'always','someone', 'look','he\'ll',
'down', 'find','ready','everything','makes', 'night','work','great','home','good','better','feel','great','bad','sad','lol','doing','everyone','nice','those','again','actually','same','before','person','true','two','days','nothing','tonight','talk','many','put','long','already','lot','tell','little','looks','something','around','years','cause','yeah','start','tell','through', 'try','such','having','awake','though','sorry','big','wish','hey','hi','help','fun','hot','miss','coming',
'thought','love','people','follow']


## retrieves only the meaningful words
def getmeaningfulwords(tweet):
    
    url = 'http://'                 
    surl = 'https://'
    words = tweet.split()
    s=''
    exclude =set(string.punctuation)  
    word_2 = []
    wordlist = []
    
    #remove all things that are 1 or 2 characters long (punctuation)
    word_1 = [word for word in words if len(word)>2]
    
    for x in word_1:
        word_2.append(x.lower())

    #get rid of all stop words
    word_3 = [word for word in word_2 if not word in STOPWORDS]
    
    #gets rid of all URL's
    word_4 = [word for word in word_3 if not word in url]
    
    #removes punctionations within words i.e. characters like # , @ , ? , etc
    for word in word_4:
        s=''.join((ch if ch not in exclude else " ") for ch in word).split()  
        for k in s:  
            if k not in STOPWORDS:
                wordlist.append(k.strip())  

    #removes word with length 2 which are created after removing all extra symbols.    
    w4 = [x for x in wordlist if len(x)>2]

    return w4

if __name__ == "__main__":
    tweets = []        
    data = []
    lines = []
    with sys.stdin as input_file:
        for obj in input_file:
            data.append(json.loads(obj))
    for line in data:
        try:        
            if line["lang"] == "en":
                #get only the tweets from the entire json object
                tweets.append(line["text"]) 
        except KeyError:
            continue 

    for tweet in tweets:
        words = getmeaningfulwords(tweet)
        for word in words:
            ## print words to stdout which will given as input to reducer.py
            print '%s\t%s' % (word.encode("utf8"), 1)
