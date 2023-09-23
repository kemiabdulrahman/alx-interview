dict = {1:1,2:2,3:3, "Fresh":{1, 2,3}}
mydict = list(dict.values())
print(mydict)

nested_dict = {
    'first_level': {
        'key1': 'value1',
        'key2': 'value2'
    },
    'second_level': {
        'key3': 'value3',
        'key4': 'value4'
    }
}

# Nested loop to print the nested dictionary one after the other
for level, inner_dict in nested_dict.items():
    print(inner_dict)
