import json

data = {
    "name" : "Trisha",   # key value pair
    "id" : 1016,
    "is_registered" : False,
    "sign_up" : None
    }

# deserialization = python to json, None, False convert to Null, false
json_string = json.dumps(data, indent = 4)
print(json_string)
print(type(json_string)) # string "" quotation not shown


# serialization = json to python
print('\n')
json_new_string = '{"name" : "Trisha","id" : 1016,"is_registered" : false, "sign_up" : null }'
python_dict = json.loads(json_new_string)
print(python_dict)
print(type(python_dict))