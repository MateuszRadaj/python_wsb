# text="Anna, paweł, Jan"
# print(type(text))
# tab=text.split(', ')
# print(tab)
# print(type(tab))
#
# name1=tab[1]
# print(name1)
#
# nameUpper = name1.upper()
# print(nameUpper)
# nameLower = name1.lower()
# print(nameLower)

#sprawdzenie zawartości
# surname=input()
# content=surname.isalpha()
# print(content)

#białe znaki
# print("jan\nKowalski")

text1 = "Jan\n"
text2 = "Kowalski"

print(text1 + text2)

text=text1.rstrip()
print(text1 + " " + text2)
print(f'{text1} {text2}')

text="%s, Java i %s" % ("PHP", "python")
print(text)

text="{1}, Java i {0}".format("PHP", "python")
print(text)

help(text.replace)
new = text.replace("PHP", "C#")
print(new)

print('test1', end='')
print('test2')
