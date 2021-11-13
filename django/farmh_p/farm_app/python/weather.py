import requests
import json 
import pandas as pd

class Weathers():
    def city():
        response = requests.get('http://api.weatherapi.com/v1/current.json?key=059cfa03f8d54ac988772656210710&q=gwangju&lang=ko&aqi=yes')
        jsonObj = json.loads(response.text)
        # print(json.dumps(jsonObj,indent=4))
        return(jsonObj['location']['name'])
    def condition():
        response = requests.get('http://api.weatherapi.com/v1/current.json?key=059cfa03f8d54ac988772656210710&q=gwangju&lang=ko&aqi=yes')
        jsonObj = json.loads(response.text)
        # print(json.dumps(jsonObj,indent=4))
        return(jsonObj['current']['condition']['text'])
    def temp():
        response = requests.get('http://api.weatherapi.com/v1/current.json?key=059cfa03f8d54ac988772656210710&q=gwangju&lang=ko&aqi=yes')
        jsonObj = json.loads(response.text)
        # print(json.dumps(jsonObj,indent=4))
        return(jsonObj['current']['temp_c'])
    def precip_mm():
        response = requests.get('http://api.weatherapi.com/v1/current.json?key=059cfa03f8d54ac988772656210710&q=gwangju&lang=ko&aqi=yes')
        jsonObj = json.loads(response.text)
        # print(json.dumps(jsonObj,indent=4))
        return(jsonObj['current']['precip_mm'])
    def humidity():
        response = requests.get('http://api.weatherapi.com/v1/current.json?key=059cfa03f8d54ac988772656210710&q=gwangju&lang=ko&aqi=yes')
        jsonObj = json.loads(response.text)
        # print(json.dumps(jsonObj,indent=4))
        return(jsonObj['current']['humidity'])
    
# ,'날씨 아이콘:',jsonObj['current']['condition']['icon']