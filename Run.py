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
