developer = {
    'name': 'Santi', 
    'last_name': 'Zuckerberg', 
    'languages': ['Javascript', 'Java', 'Python'],
    'age': 24
}

print(developer);

# REPLACE 
developer['name'] = 'Santi2';
print(developer);

developer['age'] -= 5;
print(developer);

# ADD
developer['languages'].append('R');
print(developer);

# DELETE
del developer['last_name'];
print(developer);

developer.pop('age');
print(developer);

# ITEMS, KEYS, VALUES
print('ITEMS: ');
print(developer.items());

print('KEYS: ');
print(developer.keys());

print('VALUES: ');
print(developer.values());


