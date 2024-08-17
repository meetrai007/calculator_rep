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
def sin():
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
def log():
    a=int(input("enter number:"))
    result=math.log(a)
    return result


while True:
    logging.info("""
    ###  welcome to the calculator ###
                
        choose a operation to make calculation 
                1. addition
                2. subtraction
                3. multiply
                4. devide
                5. modulus
                6. squre
                7. power of number
                8. squareroot
                9. sin
                10. cos
                11. tan
                12. log
                13. exit the application
    """)
    choice=int(input("Enter your choice 1-12 for any operation and 13 to exit:"))

    if choice==1:
        print(addition())
    if choice==2:
        print(subtraction())
    if choice==3:
        print(multiply())
    if choice==4:
        print(devide())
    if choice==5:
        print(modulus())
    if choice==6:
        print(square())
    if choice==7:
        print(powerof_number())
    if choice==8:
        print(squareroot())
    if choice==9:
        print(sin())
    if choice==10:
        print(cos())
    if choice==11:
        print(tan())
    if choice==12:
        print(log())
    if choice==13:
        print("exiting the application")
        break