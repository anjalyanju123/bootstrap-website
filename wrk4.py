# a=float(input("enter a number::"))
# if(a%7==0):
#     print("it is divisible")
# else:
#     print("not divisible")    
# b=float(input("enter a number"))
# if(b%5==0):
#     print("hello")
# else:
#     print("bye")    
# c=int(input("enter a number.."))
# c=c%10
# print(c)
# unit=float(input("enter the unit :"))
# u=5*(unit-100)
# p=500+((unit-200)*10)
# if(unit<=100):
#     print("free")
# elif(unit>=100 and unit<=200):    
#     print("total Bill=",u)
# elif(unit>200):
#     print("total Bill=",p)    
# else:
#     print("invalid input")  
r=int(input("enter a day :"))
d={1:"sunday",
   2:"monday",
   3:"tuesday",
   4:"wednesday",
   5:"thursday",
   6:"friday",
   7:"saturday"
   }
if(r==1):
    print(d[1])
elif(r==2):
    print(d[2])
elif(r==3):
    print(d[3])
elif(r==4):
    print(d[4])
elif(r==5):
    print(d[5])    
elif(r==6):
    print(d[6])    
elif(r==7):
    print(d[7])    
else:
    print("invalid input")    