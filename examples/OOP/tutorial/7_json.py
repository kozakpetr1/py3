import json
import os.path as p

class J:
    
    @staticmethod
    def check_file(func):
        def wrap(args):
            if p.isfile(args):
                return func(args)
            else:
                raise Exception("Missing JSON file.") 
        return wrap
    
    @staticmethod
    @check_file
    def load_json(path):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

json_data = J.load_json('./JSON/person.json')
print(json_data)