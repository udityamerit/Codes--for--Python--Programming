import json

data = '{"var1": 54, "var2": "harry"}'
parsed = json.loads(data)
print(parsed)


data2 = {
        "channal_name": "code_fusion",
        "cars": ["bmw", "audi a8", "farrari"],
        "fridge":("roti", 540),
        "isbad": False
}

jasoncomb = json.dumps(data2) # it is convert the data to the javascript compatible from the python

print(jasoncomb)

jsa = json.dumps(data2, sort_keys=True)
print(jsa)
