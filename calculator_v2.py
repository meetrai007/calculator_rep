import math
import logging

logging.basicConfig(level=logging.INFO)




def two_degit_calulation():
    """taking user choice to do any calculation with two num"""
    logging.debug("two degit calculation func start")
    try:
        choice = int(input("1.mul\n2.add\n3.sub\n4.dev\n5.sqr\n6.sqrt\nEnter choice:"))
        
        # if 0 <= choice <= 6:
        if 0 <= choice <= 4:
            a = int(input("enter 1st num:"))
            b = int(input("enter 2st num:"))

        if 5 <= choice <= 6:
            c = int(input("enter num:"))

        if choice == 1:
            result = a * b

        if choice == 2:
            result = a + b

        if choice == 3:
            result = a - b

        if choice == 4:
            result = a / b

        if choice == 5:
            result = c * c

        if choice == 6:
            result = math.sqrt(c)
        

        
        logging.debug("two degit calculation func end")
        return result
    except:
        print("choose a valid operation in integer 1-6")
        two_degit_calulation()

    # else:
    #     print("enter valid operation between 1-6")
    #     two_degit_calulation()


result = two_degit_calulation()
logging.info(f"\n\t\ttotal={result}\n")

while True:
    """taking user choice to add more calculation"""
    logging.info("""
                1.mul with result
                2.add num in result
                3.sub num in result
                4.dev result by a num
                5.sqr of result
                6.sqrt of result
                7.calculate new numbers
                8.exit
            """)
    try:
        choice2 = int(input("Enter choice to make calculation with result:"))
    except:
        print("Enter valid operation between 1-8")
    if choice2 == 1:
        d = int(input(f"{result}\n*"))
        result = result * d

    if choice2 == 2:
        d = int(input(f"{result}\n+"))
        result = result + d

    if choice2 == 3:
        d = int(input(f"{result}\n-"))
        result = result - d

    if choice2 == 4:
        d = int(input(f"{result}\n/"))
        result = result / d

    if choice2 == 5:
        result = result * result

    if choice2 == 6:
        result = math.sqrt(result)

    if choice2 == 7:
        result = two_degit_calulation()

    if choice2 == 8:
        break
    logging.info(f"\n\t\t result={result}\n")
