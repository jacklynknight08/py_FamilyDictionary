# Define a dictionary that contains information about several members of your family.

my_family = {
    'mother': {
        'name': 'Beth',
        'age': 50
    },
    'sister': {
        'name': 'Jessi',
        'age': 33
    },
    'brother': {
        'name': 'Joey',
        'age': 29
    },
    'father': {
        'name': 'Steve',
        'age': 50
    }
}
# Using a dictionary comprehension, produce output that looks like the following example.

# Krista is my sister and is 42 years old
# Helpful hint: To convert an integer into a string in Python, it's str(integer_value)

for key, value in my_family.items():
    print("My " + key +"'s name is " + value["name"] + " and is " + str(value["age"]) + " years old.")