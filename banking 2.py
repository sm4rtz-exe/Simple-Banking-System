import json

user_file = 'user.json'

with open(user_file, "r", encoding="utf-8") as f:
    data = json.load(f)
    users = data['users']

def save_user():
    with open(user_file,'w', encoding='utf-8') as f:
        json.dump({"users": users}, f, indent=4, ensure_ascii=False)

def login():
    while True:
        ask_user = input(str("Username: "))
        ask_password = input(str("Password: "))

        for acc in users:
            if acc['username'] == ask_user and acc['password'] == ask_password:
                print('login successfully!')
                return acc
            
        print('Username or password is incorrect')
        print('Try again')
        continue

def show_balance(user):
    print(f'Your current balance is {user["balance"]:,} usd')

def deposit(user):
    if user is None:
        print('Please Login first')
        return
    while True:
        try:
            dep = int(input('How much you want to deposit?: '))
            if dep > 0:
                user['balance'] += dep
                save_user()
                print('Deposit Procedure is completed!')
                print(f'Your current balance is {user["balance"]:,} usd')
                break
            else:
                print('The amount must be higher than 0!')
                continue
        except ValueError:
            print('You can only type numbers')
            continue

def withdraw(user):
    if user is None:
        print('Please Login first')
        return
    while True:
        try:
            if user['balance'] <= 0:
                print('You cannot withdraw')
            else:
                dep = int(input('How much you want to withdraw?: '))
                if dep > user['balance']:
                    print('Your current balance is lower than your withdraw amount')
                    continue
                elif dep > 0:
                    user['balance'] -= dep
                    save_user()
                    print('Deposit Procedure is completed!')
                    print(f'Your current balance is {user["balance"]:,} usd')
                    break
                else:
                    print('The amount must be higher than 0!')
                    continue
        except ValueError:
            print('You can only type numbers')
            continue

def change_password(user):
    while True:
        confirm = str(input('Enter your current password: '))
        if confirm != user['password']:
            print('Your password is incorrect, try again') 
            continue
            
        new_password = str(input('enter your new password: '))
        if user['password'] == new_password:
            print("New password can\'t be the same as the old password")
            print('Try again')
            continue

        ask_proceed = str(input('You can\'t undo this action, do you want to continue?\nType Y to continue/ N to cancle: '))
        if ask_proceed.lower() == 'y':
            user['password'] = new_password
            save_user()
            print('Password update successfully!')
            break
        else:
            print("Password change canceled.")
            break

def options():
    while True:
        choose = int(input('type 1 to see current balance\ntype 2 to deposit\ntype 3 to withdraw\ntype 4 to change password\ntype 5 to exit\n>>> '))
        if choose == 1:
            show_balance(current_user)
        elif choose == 2:
            deposit(current_user)
        elif choose == 3:
            withdraw(current_user)
        elif choose == 4:
            change_password(current_user)
        elif choose == 5:
            print('Goodbye!')
            exit()
        else:
            if ValueError:
                print('only receive numbers')
                print('try again')
            elif choose > 5:
                print('You can only choose 1 - 5')
                print('try again')
        continue


if __name__ == '__main__':
    current_user = login()
    options()