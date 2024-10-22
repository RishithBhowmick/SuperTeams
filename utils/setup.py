import os
import json


def setup():
    data = {}
    with open("utils/secrets.json","r") as f:
        data = json.loads(f.read())
    
    if data.get("API_KEY"):
        os.environ["REPLICATE_API_TOKEN"] = data["API_KEY"]
        _ = data.pop("API_KEY")    
    else:
        raise Exception("no api key found. Exiting...")
    
    return data