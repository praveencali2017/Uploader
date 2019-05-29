import pandas as pd
from config.default import *
from os import listdir
def search(key=None):
    filepaths=[os.path.join(UPLOAD_DIR,file) for file in listdir(UPLOAD_DIR) if file.endswith('.csv')]
    data = pd.concat(map(pd.read_csv, filepaths))
    result = data[data["Key"].str.lower()==key.lower()].to_dict('list')
    if result and 'Value' in result:
        return result['Value']
    else:
        return

# print(search("ff"))