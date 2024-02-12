# languages = ["Python", "Javascript", "PHP", "Java"];

# for language in languages:
#     print(language);

# for element in range(20):
#     print(element);

list = [23, 45, 67, 89, 43];
for i in list:
    print(i);

tuple = ('Nico', 'Juli', 'Santi');
for i in tuple:
    print(i);

dictionary = {
    'name': 'T-Shirt', 
    'price': 100,
    'stock': 89
}

for key in dictionary:
    print(key , ':' , dictionary[key]);

for key, value  in dictionary.items():
    print(key , ':' , dictionary[key]);

people = [
  {
    'name': 'nico',
    'age': 34
  },
  {
    'name': 'zule',
    'age': 45
  },
  {
    'name': 'santi',
    'age': 4
  }
]

for person in people:
  print('name =>', person['name'])