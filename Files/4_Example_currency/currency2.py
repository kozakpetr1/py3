# import urllib library
from urllib.request import urlopen
  
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
# json.dumps(data_json, indent=4)
  
# print the json response
print(json.dumps(data_json, indent=4))