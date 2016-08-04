import requests
import argparse
import json
parser=argparse.ArgumentParser()
parser.add_argument('username')
args=parser.parse_args()
obj=requests.get("https://api.github.com/users/"+ args.username)
json_data=json.loads(obj.text)
print json_data["email"]
