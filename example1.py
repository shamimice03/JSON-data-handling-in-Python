import json

# JSON Data
json_data = '''
{
    "name": "David",
    "age": 35,
    "city": "Miyazaki"
}
'''

# Parse JSON Data
data1 = json.loads(json_data)
print(f"after loads {type(data1)}")

# Convert Python object to JSON string
data2 = json.dumps(data1)
print(f"after dumps {type(data2)}")

# Output:
# after loads <class 'dict'>
# after dumps <class 'str'>