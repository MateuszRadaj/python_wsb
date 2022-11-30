# try except
# def div(x, y):
#     try:
#         result = x / y
#         return result
#     except ZeroDivisionError:
#         return 'Nie wolno dzielić przez 0!'

# print(div(3,10))

def check_user_input(input):
    try:
        val = int(input)
        print(f"Input {val} is an integer number.")
        return True
    except ValueError:
        print("No.. input is not a integer.")
        return False

while True:
    input1 = input("Enter your number ")
    if check_user_input(input1) == True:
        exit()