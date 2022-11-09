print("test")

x=10.129

print(x)

print("{:.2f}".format(x))

#potęgowanie

pow=2**10
print(pow)

#XOR ^
x=3
y=3

result= x^y

print(result)

#konkatenacja
print("Podaj swoje imie: ")
name = input()
print("Twoje imię to " + name)

length = len(name)
print(length)

firstLetter=name[0]
print(firstLetter)

print(type(name))

print("")
lastLetter = name[len(name)-1]
print("Last letter = "+lastLetter)

#konwersja
x="5"
print(type(x))
x=int(x)
print(type(x))

x=x/2
print(x, type(x))

surname = "Kowalski"
print()

print(surname[0]) #K

print(surname[0:3]) #Kow

print(surname[-2]) #k

print(surname[:-2:2]) #Kwl
