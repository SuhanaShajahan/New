import math
def square(num):
    s=math.sqrt(num)
    flag=False
    for i in range(1,num):
        if s==i:
            flag=True
    if flag==True:
        print(num,"is perfect")
    else:
        print(num,"is not perfect")

num=int(input("Enter a number:"))
square(num)