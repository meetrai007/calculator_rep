import math
import logging

logging.basicConfig(level=logging.INFO)

def addition():
    a=int(input("enter 1st number:"))
    b=int(input("enter 2st number:"))
    result=a+b
    return result
def subtraction():
    a=int(input("enter 1st number:"))
    b=int(input("enter 2st number:"))
    result=a-b
    return result
def multiply():
    a=int(input("enter 1st number:"))
    b=int(input("enter 2st number:"))
    result=a*b
    return result
def devide():
    a=int(input("enter 1st number:"))
    b=int(input("enter 2st number:"))
    result=a/b
    return result
def modulus():
    a=int(input("enter 1st number:"))
    b=int(input("enter 2st number:"))
    result=a%b
    return result
def square():
    a=int(input("enter number:"))
    result=a+a
    return result
def powerof_number():
    a=int(input("enter  number:"))
    b=int(input("enter power of number:"))
    result=a**b
    return result
def squareroot():
    a=int(input("enter number:"))
    result=math.sqrt(a)
    return result
def sign():
    a=int(input("enter number:"))
    result=math.sin(a)
    return result
def cos():
    a=int(input("enter number:"))
    result=math.cos(a)
    return result
def tan():
    a=int(input("enter number:"))
    result=math.tan(a)
    return result

print(tan())