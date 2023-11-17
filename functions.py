from collections import Counter
from spacy import displacy
import lists

#SUBSIDIARY FUNCTIONS

def word_counter(word_list, word_number):
    
    cnt = Counter()
    for numbers in word_list:
        cnt[numbers] +=1

    result = dict(cnt)
    result = sorted(result.items(), key=lambda x:x[1], reverse=True)
    
    return (dict(result[0:word_number]))

def input_text():
    
    text = ''
    
    print('Enter text')
    text = input()
    
    return text
    
def doc_to_sents(doc):
    
    sents_list = []
    
    for sent in doc.sents:
        
        sentence = sent.text
        sents_list.append(sentence)
        
    return sents_list

#PRIMARY FUNCTIONS

#1.Counting nouns:

def noun_count(doc):
    
    noun_list = []
    
    for token in doc:
        
        if token.pos_=='NOUN' and token.text not in lists.ttl:
            token_text = token.text
            noun_list.append(token_text)
    
    noun_counted = word_counter(noun_list, 10)
    
    return noun_counted

#2.Extracting entites which are not numbers:

def entities_count(doc):
    
    entities_dict = {}
    dates_list = []
    orgs_list = []
    numbers_list = []
    
    for ent in doc.ents:
        
        if ent.label_ == 'DATE':
            
            if ent.text not in dates_list:
        
                dates_list.append(ent.text)
            
        elif ent.label_ == 'ORG':
            
            if ent.text not in orgs_list:
            
                orgs_list.append(ent.text)
        
        elif ent.label_ == 'MONEY' or ent.label_ == 'PERCENT':
            
            if ent.text not in numbers_list:
            
                numbers_list.append(ent.text)
            
    entities_dict = {
        "Dates": dates_list,
        "Orgs": orgs_list,
        "Numbers": numbers_list
    }
        
    return entities_dict
    
#3.Visualizing entities
    
def visualize_entities(doc):

    displacy.render(doc, style="ent")

#4.Extracting noun chunks:

def chunks_extraction (doc):
    
    chunks_list = []
    
    for chunk in doc.noun_chunks:
        
        if chunk.text not in chunks_list:
        
            chunks_list.append(chunk.text)
        
    return chunks_list

#5.Find sentence

def find_sents(text, sents_list):
    
    found_sents = []
    
    for sent in sents_list:
        
        if text in sent:
            
            found_sents.append(sent)
            
    return found_sents