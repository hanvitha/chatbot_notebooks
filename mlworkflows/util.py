import numpy as np

import os
import cloudpickle as cp

def clean_up_sentence(sentence):
    # tokenize the pattern
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words

def bow(sentence, words, show_details=False):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words
    bag = [0]*len(words)  
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)

    return(np.array(bag))

def serialize_to(obj, default_filename):
    filename = os.getenv("S2I_PIPELINE_STAGE_SAVE_FILE", default_filename)
    cp.dump(obj, open(default_filename, "wb"))
    cp.dump(obj, open(filename, "wb"))

def sample_corresponding(count, source, *sources, **kwargs):
    """ given one or more list-like or data-frame-like sources, sample _count_ elements
    from each such that corresponding elements are returned. """
    
    if "seed" in kwargs:
        np.random.seed(int(kwargs["seed"]))
    
    replace = False
    
    if "replace" in kwargs:
        replace = kwargs["replace"]
        
    indices = np.random.choice(source.shape[0], count, replace=replace)
    def extract(s, idxs):
        if hasattr(s, "iloc"):
            return s.iloc[idxs, :]
        else:
            return s[idxs, :]

    return [extract(s, indices) for s in [source] + list(sources)]

