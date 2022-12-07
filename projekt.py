def podatek(salary):
    print(f'Jestem w podatek {salary}')
    return


def wyplata():
    salary = int(input("Wprowadź swoją wypłatę (netto): "))
    print(f'Roczny dochód wynosi {salary*12}')
    return salary

def menu():
    print("0. Wyjdź z aplikacji")
    print("1. Wprowadź swoją wypłatę")
    print("2. Pokaż ile podatku muszę zapłacić")

    wybor = int(input("Wybierz opcje: "))
    salary = 0

    while wybor != 0:
        if wybor == 1:
            salary = wyplata()
        elif wybor == 2:
            podatek(salary)

menu()
