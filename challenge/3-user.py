#!/usr/bin/python3
"""
A User class
"""
import hashlib

class User:
    """
    Definition of the User class
    """
    def __init__(self):
        self.__password = None

    @property
    def password(self):
        """password getter"""
        return self.__password

    @password.setter
    def password(self, pwd):
        """password setter"""
        if type(pwd) is not str:
            self.__password = ""
        else:
            self.__password = hashlib.md5(pwd.encode()).hexdigest()

    def is_valid_password(self, pwd):
        """checks if the password is valid"""
        if type(pwd) is not str:
            return False
        if self.__password is None:
            return False
        return hashlib.md5(pwd.encode()).hexdigest() == self.__password

if __name__ == "__main__":
    u = User()
    u.password = "holberton"
    if u.is_valid_password("holberton"):
        print("is_valid_password should return True if it's the right password")
    else:
        print("is_valid_password should return False if it's the wrong password")
