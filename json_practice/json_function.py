import json
 
def write_json(new_data, filename='hi/hi.json'):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["menu"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)


def print_json(filename='hi/hi.json'):
    with open(filename,'r') as file:
        data = json.load(file)
        print(data)

print_json()
z = {}

z['first_name'] = input("Insert your first name:")
z['last_name'] = input("Insert your last name:")
z['email'] = input("Insert your email:")

print(z)

write_json(z)
