from collections import Counter
from spacy import displacy

#trash token list (words, which are potentially useless)

ttl = ['Q1', 'quarter', '%', 'year', 'question', 'business', 'thanks']

#SUBSIDIARY FUNCTIONS

def word_counter(word_list, word_number):
    
    cnt = Counter()
    for numbers in word_list:
        cnt[numbers] +=1

    result = dict(cnt)
    result = sorted(result.items(), key=lambda x:x[1], reverse=True)
    
    return (dict(result[0:word_number]))

#PRIMARY FUNCTIONS

#1.Counting nouns:

def noun_count(doc):
    
    noun_list = []
    
    for token in doc:
        
        if token.pos_=='NOUN' and token.text not in ttl:
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