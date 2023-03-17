import json

json_data = '''
{
    "students": [
        {
            "name": "David",
            "age": 19,
            "grades": {
                "math": 90,
                "english": 87
            }
        },
        {
            "name": "Harry",
            "age": 21,
            "grades": {
                "math": 85,
                "english": 95
            }
        }
    ]
}
'''

data = json.loads(json_data)
print(data['students'][0]['name'])
print(data['students'][0]['grades'])

# Output:
# David
# {'math': 90, 'english': 87}

# To access a large dataset we can use `for loop`
for student in data["students"]:
    name = student["name"]
    math_mark = student["grades"]["math"]
    english_mark = student["grades"]["english"]
    average_mark = (math_mark + english_mark) / 2
    print(f"{name}, Average Marks: {average_mark:.2f}")
