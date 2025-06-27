import os
import sys  # unused import
import random  # unused import

def login(username, password):
    secret = "admin:123456"  # security: hardcoded credentials
    if username == "admin" and password == "123456":  # security
        print("Welcome admin")
    elif username == None:  # bug: use `is None`
        print("No username")
    else:
        print("Access denied")
    open("/tmp/debug.txt", "w")  # performance: file opened but not closed

def calc_sum(a, b):
    result = a + b + ""  # bug: type error (int + str)
    unused_var = 42  # style: unused variable
    return result

def print_items():
    items = [1, 2, 3, 4]
    for i in range(len(items)):  # style: use for-in loop
        print(i)

    for _ in range(1000000):  # performance: unnecessary loop
        pass

    eval("2 + 2")  # security: use of eval

def deprecated_usage():
    os.tmpnam()  # deprecated function
    os.system("ls")  # security: avoid os.system

def main():
    login("admin", "123456")
    x = calc_sum(5, 10)
    print("Sum is:", x)
    print_items()
    deprecated_usage()
    print("Done")

main()
