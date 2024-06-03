print("-----------------Welcome to ATM------------------------")
Username = "harika"
Password = "1234"

user = input("Enter Username: ").lower()
pass1 = input("Enter Password: ")

s = """1.Credit
2.Debit
3.Ministatement
4.Exit
    """
current_balance = 10000

if Username == user and Password == pass1:
    while True:
        print(s)
        option = int(input("Choose one option among the above: "))
        if option ==1:
            add = float(input("Enter the credit amount: "))
            current_balance = current_balance+add
            print("Amount after credit",current_balance)
        elif option == 2:
            sub = float(input("Enter how much amount needed to debit: "))
            current_balance = current_balance-sub
            print("Amount after debit",current_balance)
        elif option ==3:
            print(current_balance)
        else:
            print("Thank you! Visit Again")
            break
else:
    print("Username or Password are incorrect! Try again")
    

    
    

