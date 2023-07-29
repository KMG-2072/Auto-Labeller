import json

def read_input(file):
    with open(file,'r') as file:
        text=file.read()
        out_json=json.loads(text)
    return out_json
def generate_PolyBox(Polygon):
    poly_list=[]
    count=0
    for x,y in [(Polygon[i],Polygon[i+1]) for i in range(0,len(Polygon),2)]:
        cord_dict = {}
        cord_dict['x']=x
        cord_dict['y']=y
        poly_list.append(cord_dict)
    return poly_list
def generate_word_dict(word,page_index):
    word_dict={}
    word_dict['boundingPoly']={'vertices':generate_PolyBox(word['Polygon'])}
    word_dict['description']=word['Text']
    word_dict['score']=word['OcrConfidence']
    word_dict['line']=word['VisualLineNumber']
    word_dict['page']=page_index
    word_dict['tag']=''
    return word_dict

def generate_dictionary(DOM):
    '''This function will generate a dictionary containing all the
    \tParameters:\tDOM- Document Object Model as a Json file
    '''
    text_list=[]
    for Section in DOM['Pages'][0]['Sections']:
        for WordGroup in Section['WordGroups']:
            for Word in WordGroup["Words"]:
                text_list.append(generate_word_dict(Word,0))

    return text_list

with open('word_dict.txt','w') as file:
    file.write(json.dumps(generate_dictionary(read_input('DOM_125.txt')),indent=4))
    