from os import write
import pandas as pd
import json

with open('translation.json', 'r') as openfile:   
    # Reading from json file 
    json_object = json.load(openfile) 

excel = pd.read_excel("out.xlsx") 
#print(excel.head())

json_object['cultures'][0]['translations']['model']['translatedCaption']="التعليق"
json_object['cultures'][0]['translations']['model']['translatedDescription']="الوصف"
"""
"""
for i in range(len(json_object['cultures'][0]['translations']['model']['tables'])):
    """
    for column in table['columns']:
        trans = excel[(excel['table_name']==table['name']) & (excel['column_name']==column['name'])][['translatedCaption','translatedDescription']]
        column['translatedCaption']=trans['translatedCaption'].iloc[0]
        column['translatedDescription']=trans['translatedDescription'].iloc[0]
        print(column)
    """
    for j in range(len(json_object['cultures'][0]['translations']['model']['tables'][i]['columns'])):
        trans = excel[(excel['table_name']==json_object['cultures'][0]['translations']['model']['tables'][i]['name']) & (excel['column_name']==json_object['cultures'][0]['translations']['model']['tables'][i]['columns'][j]['name'])][['translatedCaption','translatedDescription']]
        json_object['cultures'][0]['translations']['model']['tables'][i]['columns'][j]['translatedCaption']=trans['translatedCaption'].iloc[0]
        json_object['cultures'][0]['translations']['model']['tables'][i]['columns'][j]['translatedDescription']=trans['translatedDescription'].iloc[0]
        #print(json_object['cultures'][0]['translations']['model']['tables'][i]['columns'][j])
        



json_object=json.dumps(json_object)
with open('json_data.json', 'w') as outfile:
    outfile.write(json_object)
