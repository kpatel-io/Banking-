import pickle
import pathlib
import os

def transfer():
    
    
    type1 = print(input("Would you like to transfer from Checking to Savings? (yes or no) "))
    if type1 == "yes":
            amount = float(input("Enter the amount to Transfer: "))
            Checking.withdraw(amount)
            if(Checking.withdraw(amount) ==True):
                Savings.deposit(amount)

    type2 = print(input("Would you like tro transfer from Savings to Checking? (yes or no) "))
    if type1 == "yes":
            amount = float(input("Enter the amount to Transfer: "))
            Savings.withdraw(amount)
            if(Savings.withdraw(amount) ==True):
                Checking.deposit(amount)

class customer():
    def __init__ (self, FirstName, LastName, address):
        self.FirstName = "FirstName"
        self.LastName = "LastName"
        self.Address = "address"

    def person():
        Firstname = input("Enter your First Name: ")
        LastName = input("Enter your Last Name: ")
        Address = input("Enter your Address: ")
        
    def details (self):
        print("Customer Details ")
        print( " ")
        print(" Name: ", self.FirstName, " " , self.LastName)
        print(" Address ", self.Address)


class accounts():
  
    def __init__(self):
        self.balance = 0
        print("")

    def deposit(self,amount):
        self.balance += amount
        print("Your new  balance is ", self.balance)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(" You withdrew ", amount)
            return True
        else: 
            print("insufficiant balance: Your balance is ", self.balance )
            return False
        
  
    def display(self):
        print("Your balance is ", self.balance)
    


print("Welcome to Spring Bank")
C = customer.person()
Checking = accounts()
amount = float(input("Enter the amount to Deposit: "))
Checking.deposit(amount)
if Checking.balance >=0:
    print("Checking Account Successful")
else:
    print("Checking Account Unsuccessful")


Savings = accounts()
amount = float(input("Enter the amount to Deposit: "))
Savings.deposit(amount)
if Savings.balance >=0:
    print("Savings Account Successful")
else:
    print("Savings Account Unsuccessful")

print("Would You like to transfer between Savings and checking? (yes or no) ")

transfer()




