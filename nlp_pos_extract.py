import spacy
from nlp_strategy import *

nlp = spacy.load('en_core_web_md')

def pre_processing(sentence):
    expand = expand_contractions(sentence)
    lemmetize = lemmatize_text(expand)
    stopwords = remove_stopwords(lemmetize)
    return stopwords.lower()

def extract_info(doc):
    action = ""
    what = ""
    participants = ""
    for token in doc:
        if token.lemma_=="send" and token.pos_=="VERB" and token.dep_=="ROOT":
            children = [child for child in token.children]
            action = token.lemma_
            for child1 in children:
                # the what - dobj - direct object
                if child1.dep_=="dobj":
                    what += " ".join([attr.text for attr in child1.children]) + " " + child1.text + " "
                elif child1.text=="to":
                    child1_children = [child for child in child1.children]
                    for child2 in child1_children:
                        if child2.pos_ == "NOUN":
                            participants += " ".join([attr.text for attr in child2.children]) + " " + child2.text + " "
    print (f"action = {action}") # send
    print (f"what = {what}")   # priority message
    print (f"To = {participants}")  # tanvi, aruj, naveena
    return {
        "data": {
            "action": action,
            "what": what,
            "to": participants
        }
    }

# nlp_it("Help me send a priority message to Tanvi and Aruj")
def nlp_it(dictate):
    doc = nlp(pre_processing(dictate))
    print(f"Sentence = {dictate}")
    return extract_info(doc)
