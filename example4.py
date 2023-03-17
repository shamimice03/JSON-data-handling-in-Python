import json

original_data_file="students_data.json"
updated_data_file="students_data_updated.json"

# reading `JSON file`
with open(original_data_file,"r") as file:
   students_result = json.load(file)

# Updating JSON Data
for student in students_result['students']:
    print(student['name'])
    
    if student['name'] == "Kabir":
        student['name'] = "John"
        
    grades = student['grades']
    average_mark = sum(grades.values()) / len(grades)
    student['avarage_mark'] = average_mark

# Saving updated data into a new file
with open(updated_data_file,"w") as file:
    json.dump(students_result,file,indent=4)