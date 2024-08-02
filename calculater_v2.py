import  math


total=0

"""taking user choice to do any calculation"""
print(f"\t\ttotal={total}\n")
choice=int(input("1.mul\n2.add\n3.sub\n4.dev\n5.sqr\n6.sqrt\n7.exit\n\nEnter choice:"))

if 0<=choice<=4:
    a=int(input("enter 1st num:"))
    b=int(input("enter 2st num:"))
if 5<=choice<=6:
    c=int(input("enter num:"))


if choice==1:
    total=a*b
    print(f"\n\t\ttotal={total}\n")
    
if choice==2:
    total=a+b
    print(f"\n\t\ttotal={total}\n")
    
if choice==3:
    total=a-b
    print(f"\n\t\ttotal={total}\n")
    
if choice==4:
    total=a/b
    print(f"\n\t\ttotal={total}\n")

if choice==5:
    total=c*c
    print(f"\n\t\ttotal={total}\n")

if choice==6:
    total=math.sqrt(c)
    print(f"\n\t\ttotal={total}\n")
    
while True:
    """taking user choice to add more calculation"""
    choice=int(input("1.mul with total\n2.add num in total\n3.sub num in total\n4.dev total by a num\n5.sqr of total\n6.sqrt of total\n7.exit and calculate new num\n\nEnter choice to make calculation with total:"))
    

    if choice==1:
        d=int(input(f"{total}\n*"))
        total=total*d
        print(f"\n\t\ttotal={total}\n")
    
    if choice==2:
        d=int(input(f"{total}\n+"))
        total=total+d
        print(f"\n\t\ttotal={total}\n")
        
    if choice==3:
        d=int(input(f"{total}\n-"))
        total=total-d
        print(f"\n\t\ttotal={total}\n")
        
    if choice==4:
        d=int(input(f"{total}\n/"))
        total=total/d
        print(f"\n\t\ttotal={total}\n")

    if choice==5:
        total=total*total
        print(f"\n\t\tsquare of total is {total}\n")

    if choice==6:
        total=math.sqrt(total)
        print(f"\n\t\tsquareroot of total is {total}\n")
    
    if choice==7:
        break

