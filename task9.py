import random
user = input("Enter symbols 'R' - Rock; 'S' - scissors; 'P' - paper: ")
RSP_list = ['R', 'S', 'P']
random_RSP = random.choice(RSP_list)
while user == 'R' or 'S' or 'P':
    if user == 'R' and random_RSP == 'S':
        print(f"User - {user}, Bot - {random_RSP}, USER WINNER!")
        send = input("Maybe again? Yes/No ")
        if send == 'No':
            break
    elif user == 'S' and random_RSP == 'P':
        print(f"User - {user}, Bot - {random_RSP}, USER WINNER")
        send = input("Maybe again? Yes/No ")
        if send == 'No':
            break
    elif user == 'P' and random_RSP == 'P':
        print(f"User - {user}, Bot - {random_RSP}, USER WINNER")
        send = input("Maybe again? Yes/No ")
        if send == 'No':
            break
    elif user == 'R' and random_RSP == 'R':
        print(f'User - {user}, Bot - {random_RSP}, DRAW!')
        send = input("Maybe again? Yes/No ")
        if send == 'No':
            break
    elif user == 'S' and random_RSP == 'S':
        print(f'User - {user}, Bot - {random_RSP}, DRAW!')
        send = input("Maybe again? Yes/No ")
        if send == 'No':
            break
    elif user == 'P' and random_RSP == 'P':
        print(f'User - {user}, Bot - {random_RSP}, DRAW!')
        send = input("Maybe again? Yes/No ")
        if send == 'No':
            break
    elif user == 'R' and not random_RSP == 'S':
        print(f'User - {user}, Bot - {random_RSP}, LOSE!')
        send = input("Maybe again? Yes/No ")
        if send == 'No':
            break
    elif user == 'S' and not random_RSP == 'P':
        print(f'User - {user}, Bot - {random_RSP}, LOSE!')
        send = input("Maybe again? Yes/No ")
        if send == 'No':
            break
    elif user == 'P' and not random_RSP == 'R':
        print(f'User - {user}, Bot - {random_RSP}, LOSE!')
        send = input("Maybe again? Yes/No ")
        if send == 'No':
            break