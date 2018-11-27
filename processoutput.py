import json
from pprint import pprint


# Load params:
with open('artifacts.json') as data_file:    
        data = json.load(data_file)
        pprint(data)



BucketnameOutput=(data["BucketnameOutput"]["value"])

print(BucketnameOutput)