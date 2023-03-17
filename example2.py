import json

json_data = '''
{
    "name": "David",
    "age": 35,
    "city": "Miyazaki",
    "pets": [
        {
            "name": "tom",
            "type": "cat"
        },
        {
            "name": "jerry",
            "type": "mouse"
        }
    ]
}
'''

# Parse JSON Data
data = json.loads(json_data)

# Accessing Data
print(f"Name is: {data['name']}")
print(f"Name is: {data['pets']}")

# Accessing Nested JSON data
for item in data['pets']:
    print(f"Pet Name: {item['name']}")

# Outputs:

# Name is: David
# Name is: [{'name': 'tom', 'type': 'cat'}, {'name': 'jerry', 'type': 'mouse'}]
# Pet Name: tom
# Pet Name: jerry
