country = ['Germany', 'France', 'Spain', 'Poland', 'Austria']

add_country = []

add_country.append(input('Input country name: '))
add_country.append(input('Input country name: '))

country.extend(add_country)

ans=True
while ans:
    print ("""
    1.Show three first elements
    2.Show elements added by me
    3.Show all elements
    4.Clear list
    5.Find element by name
    """)
    ans=input("\n What would you like to do? ") 
    if ans=="1": 
      print(str(country[0:3]))
      break
    elif ans=="2":
      print("\n Added: ", str(add_country))
      break
    elif ans=="3":
      print("\n Countries: ", str(country))
      break
    elif ans=="4":
        country.clear()
        print("\n CLEARED!")
        break
    elif ans=="5":
        look_for = input("\n Name of country: ")
        
        def search(list, x):
            for i in range(len(list)):
                if list[i] == x:
                    return True
            return False
        
        if search(country, look_for):
            print('\n Country found in list')
        else:
            print('\n Country not found in list')
        break
    elif ans !="":
      print("\n Not Valid Choice Try again")

print('\n Your list of countries: ', str(country))
print()
