programowanie=['Python', 'PHP', 'C#', 'JS', 'Java']
print(programowanie)

lastElement = programowanie[-1]
print("Ostatni: ", lastElement)

programowanie.append('R')
programowanie.append('Python')
print(programowanie)

countElements=programowanie.count('Python')
print(countElements)

countElementsOfList=len(programowanie)
print(type(countElementsOfList))
print('Ilość elementów w liście ' + str(countElementsOfList))

anotherList=['C', 'C++']
programowanie.extend(anotherList)
print('Lista programowanie: ', str(programowanie))
print('Lista programowanie: ', str(anotherList))

new = programowanie
print('new list: ' + str(new))
new.clear()
print('new list again: ' + str(new))
print('rozmiar new list: ' + str(len(new)))

x=8
print(x)
y=x
print(y)

y = 5
print(x)
print(y)

