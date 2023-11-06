#gonna use later

def add_date(date):
    
    date = ''
    
    print('Enter date')
    date = input()
    
    return date

def metadata_extraction(doc, features_list):
    
    if 'noun_count' in features_list:
        noun_count(doc)
        
    return metadata_extraction

features_list = ['noun_count', 'entities']
    
meta_extraction(doc, features_list)