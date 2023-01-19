user_input = int(input("Enter numbers: "))
num = 0
while user_input >= num:
    if num % 2:
        print(num,'ODD')
    else:
        print(num,"EVEN")
    num = num + 1
