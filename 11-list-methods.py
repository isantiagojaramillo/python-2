languages = ["Python", "Javascript", "PHP", "Java"];
languages.insert(3, "Go");
languages.insert(0, "C");
languages.remove("Java");
languages.append("ReactJS");
print(languages);

print("PHP" in languages);
# languages.clear();


print(len(languages));

tasks = ['todo 1', 'todo 2', 'todo 3'];
new_list = languages + tasks;
print(new_list);

index = new_list.index('todo 2');
new_list[index] = 'todo changed';
print(new_list);

new_list.pop();
print(new_list);

new_list.pop(0);
print(new_list);

new_list.reverse();
print(new_list);

numbers = [1, 4, 6 , 3];
numbers.sort();
print(numbers);

strings = ['re', 'ab', 'ed'];
strings.sort();
print(strings);

new_list.sort();
