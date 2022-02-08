import pandas as pd
import json

with open('translation.json', 'r') as openfile: 
  
    # Reading from json file 
    json_object = json.load(openfile) 

    
tables_object = json_object['referenceCulture']['model']['tables']
table_names = []
column_names = []
result = pd.DataFrame(columns=['table_name', 'column_name'])
for table in tables_object:
    columns_object = table['columns']
    current_table_columns = []
    for column in columns_object:
        current_table_columns.append(column['name'])
    result.loc[len(result)]=[table['name'], current_table_columns]

result = pd.DataFrame([{'table_name':tup.table_name, 'column_name':c} for tup in result.itertuples() for c in tup.column_name])
result.to_csv('out.csv',index=False)