#!/usr/bin/env python3.6
from Plocker import User
import random
from Plocker import Password

def create_user(username,password,accountName):
    '''
    Function to create a new user
    '''
    user_details=User(username,password,accountName)
    return user_details

def save_user(Plocker):
    '''
    Function to save a new user
    '''
    Plocker.create()


def delete_password(username,password,accountName):
    '''
    Function  to delete password
    '''
    user_details=User(username,password,email)
    return user_details

def delete_account(Plocker):
    '''
    Function to delete account
    '''
    Plocker.delete()

def display_passwords():
    '''
    Function to display all passwords
    '''
    return User.display_user()


def search_account(number):
    '''
    Function to search for account
    '''
    return User.find_by_accountName(number)

def check_account_existence(number):
    '''
    Function to check if account exists
    '''
    return User.account_exist(number)


def random_password(limit):
    '''
    Function to create random password
    '''
    password="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    run=len(password)
    hold=''
    for i in range(0,limit):
        all=password[random.randint(0,run)]
        hold=hold+all
    return hold



def main():
        print("Hello! Welcome to your Password Locker.Sign up below")
        print("Enter your userName")
        name=input()
        print("Use g to generate password or m to make your own password")
        short_codes=input().lower()
        if short_codes=="g":
            print("Enter the length that you would like your password to have. Recommended length:)5")
            limit=int(input())
            password=random_password(limit)
            print("Your password is "+password)
        else:
            print("Enter your password")
            password=input()
        thisAccount="passwordLocker"
        save_user(create(User,password,name))
        print("\n")
        print(f"Welcome {name}! Please Login below")
        print("Enter the username that you just created")
        User=input()
        print("enter your password ")
        Password=input()
        if User==name and Password==password:
            print("\n")
            print(f"Welcome to your dashboard {name}")
            while True:
                print("These are short code to help you navigate through\n sp- save new password dp-- display all passwords fa-- find a specific account password  dp-- delete password ex-- exit this application")
                short_codes=input().lower()
                if short_codes=="sp":
                    print("-"*20)
                    print("Are you ready to create a new password?\n")
                    print(f"{name} Please enter the account name you need to be saved eg-Instagram | Facebook | Github")
                    thisAccount=input()
                    print("Enter username")
                    username=input();
                    print("Enter the password and make sure no one is watching")
                    password=input()
                    thisAccount="passwordLocker"
                    save_user(create(thisAccount,username,password))
                    print("\n")
                    print(f"{thisAccount} account details saved succefully")
                    print("\n")

                elif short_codes=="dp":
                    if display_passwords():
                        print(f"{name} These are all your passwords,make sure you keep them safe")
                        print("--"*40)
                        print("Account Name \t  Username\t password")
                        print("_"*60)
                        for account in display_passwords():
                            print(f"{account.username} \t {account.password}............{account.email}")
                            print("\n")
                        print("--"*40)
                    else:
                        print("\n")
                        print("It seems you have not Accounts yet")

                elif short_codes=="fa":
                    print("Enter Account name")
                    search_pass=input();
                    if check_account_existence(search_pass):
                        searchP=search_account(search_pass)
                        print("\n")
                        print("Account Match ------1")
                        print("Username\t password")
                        print("__"*20)
                        print(f"{searchP.password}...\t{searchP.email}")
                        print("--"*20)
                        print("\n")
                    else:
                        print("That Account does not exist Please Try again")
                        print("--"*20)
                        print("\n")

                elif short_codes=="dp":
                    print("Enter Account Name to be deleted")
                    delAccount=input();
                    if check_account_existence(delAccount):
                        for i in display_passwords():
                            if delAccount in i.username:
                                posi=display_passwords().index(i)
                        display_passwords().remove(display_passwords()[posi])
                        print("\n")

                        print(f"{delAccount} Account deleted succefully")
                        print("\n")
                    else:
                        print("That acount does not exist")

                elif short_codes=="ex":
                    print("are you sure about this \n yes or no")
                    sure=input().lower()
                    if sure=="no":
                        continue
                    else:
                        print("see yah later...Bye!!!")
                        break
                else:
                    print("Invalid!...would you please use the short codes")
        else:
            print("wrong username or password")

if __name__ == '__main__':
    main()
