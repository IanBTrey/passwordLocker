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
