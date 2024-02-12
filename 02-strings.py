# STRING METHODS

text = "Hello Santi";

print(text.upper());
print(text.lower);
print(text.find("S"));
print(text.find("Santi"));
print(text.replace("San", "Happy Chanchito"));
newText = text.replace("San", "Happy Chanchito");
print(text, newText);
print("Hello" in text);

print(text.count('a'));

print(text.swapcase());
print(text.startswith('She'));
print(text.endswith('Rust'));
print(text.replace('Santi', 'Python'));

print(text[0:5]);
print(text[10:16]);
print(text[:10]);
print(text[5:-1]);
print(text[5:]);
print(text[:]);
print(text[10:16:1]);
print(text[10:16:2]);
print(text[::2]);

text_2 = 'este es un titulo';
print(text_2);
print(text_2.capitalize());
print(text_2.title());
print(text_2.isdigit());
print("398".isdigit());

size = len(text_2);
print("Size: "+size);

print(text_2[size -1]);
print(text_2[-1]);

