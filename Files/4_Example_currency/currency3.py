# import urllib library
from urllib.request import urlopen
import pandas as pd
 
# import json
import json
# store the URL in url as 
# parameter for urlopen
url = "https://data.kurzy.cz/json/meny/b[1].json"

# store the response of URL
response = urlopen(url)
  
# storing the JSON response 
# from url in data
data_json = json.loads(response.read())

foo = open("kurzy.json", "wt", )
foo.write(str(json.dumps(data_json, indent = 4)))
foo.close()
#print(df)

with open("kurzy.json",'r') as f:
    data = json.loads(f.read())
f.close()

# Flatten data
# df_nested_list = pd.json_normalize(data, record_path =['kurzy'])
df_nested_list = pd.json_normalize(data)
with open("kurzy.tbl", "wt") as f:
    f.write(str(df_nested_list))
f.close()