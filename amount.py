#challenge program from lahari madam

user_name=input("Enter your Username:")
user_number=int(input("Enter your User Mobile Number:"))
user_mailId=input("Enter your Mail ID:")
amount=int(input("Enter the Amount:"))
print(" 1.User Details\n 2.Update User Details\n 3.Update Amount\n 4.Verify Ammount\n 5.Exit")
while 1:
    choice=int(input("Enter your choice:"))
    if choice==1:
        print("User Details:")
        print("Name:",user_name)
        print("Number:",user_number)
        print("Mail ID:",user_mailId)
    elif choice==2:
        user_name=input("Enter your name:")
        user_number=int(input("Enter your number:"))
        user_mailId=input("Enter your mail ID:")
        print("User Details Updated Successfully")
    elif choice==3:
        print("1.Credit\n2.Debit")
        transaction_type=int(input("Enter the transaction type:"))
        if transaction_type==1:
            Updated_amount=int(input("Enter the amount to credit:"))
            if Updated_amount<0:
                print("Invalid amount")
            else:
                amount=amount+Updated_amount
                print("Amount Credited successfully")
        elif transaction_type==2:
            Updated_amount=int(input("Enter the amount to debit:"))
            if Updated_amount>amount:
                print("Insufficient balance")
            else:
                amount=amount-Updated_amount
                print("Amount Debited successfully")
        else:
            print("Invalid transaction type")
    elif choice==4:
        print(amount)
    elif choice==5:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")