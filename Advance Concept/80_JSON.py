import json

data = '{"var1": 54, "var2": "harry"}'
parsed = json.loads(data)
print(parsed)
