dictionary = {};
print(type(dictionary));

dictionary = {
    'airplane': 'NGAD',
    'name': 'Santi',
    'last_name': 'Maverick',
    'age': 24
}

print(dictionary);
print(len(dictionary));

print(dictionary['age']);
print(dictionary['last_name']);

print(dictionary.get('nonexistent_key'));
print(dictionary.get('age'));

print('airplane' in dictionary);
print('nonexistent_key' in dictionary);
