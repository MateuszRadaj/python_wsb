while True:
    try:
        x = float(input("Bok kwadratu "))
    if x <= 0:
        raise NullValueError
    print(f"Pole kawdratu wynosi {x**2}")
    break

    except ValueError:

    except NullValueError:
