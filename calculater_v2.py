import  math
import logging
logging.basicConfig(level=logging.INFO)


"""taking user choice to do any calculation"""

def two_degit_calulation():
    logging.debug("two degit calculation func start")
    choice=int(input("1.mul\n2.add\n3.sub\n4.dev\n5.sqr\n6.sqrt\nEnter choice:"))

    if 0<=choice<=4:
        a=int(input("enter 1st num:"))
        b=int(input("enter 2st num:"))
    if 5<=choice<=6:
        c=int(input("enter num:"))

    if choice==1:
        result=a*b
        
    if choice==2:
        result=a+b
        
    if choice==3:
        result=a-b
        
    if choice==4:
        result=a/b

    if choice==5:
        result=c*c

    if choice==6:
        result=math.sqrt(c)
    
    logging.debug("two degit calculation func end")
    return result


result=two_degit_calulation()
logging.info(f"\n\t\ttotal={result}\n")

while True:
    """taking user choice to add more calculation"""
    choice=int(input("1.mul with result\n2.add num in result\n3.sub num in result\n4.dev result by a num\n5.sqr of result\n6.sqrt of result\n7.calculate new numbers\n8.exit\nEnter choice to make calculation with result:"))
    

    if choice==1:
        d=int(input(f"{result}\n*"))
        result=result*d
    
    if choice==2:
        d=int(input(f"{result}\n+"))
        result=result+d
        
    if choice==3:
        d=int(input(f"{result}\n-"))
        result=result-d
        
    if choice==4:
        d=int(input(f"{result}\n/"))
        result=result/d

    if choice==5:
        result=result*result

    if choice==6:
        result=math.sqrt(result)
    
    if choice==7:
        result=two_degit_calulation()
        
    if choice==8:
        break
    logging.info(f"\n\t\t result={result}\n")

