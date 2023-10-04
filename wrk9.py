# program for printing first letter of each word capitalized
# name=str(input("enter the name:"))
# def myname():
#   result = name.title()
#   return result
# print(myname())
# program to remove all special characters
# sentence=input("enter the string:")
# def character():
#     charact=" "
#     for i in sentence:
#         if i.isalpha():
#              charact+=i
#     print(charact)

# character()
# program to print sum of square of numbers
# def square():
#    num=input("enter the numbers:")
#    sq=0
#    for i in num:
#      print(i)
#      sq+=(int(i)**2)
#      print(sq)  

# square() 

# program to print common elements in two lists 
# list1=[]
# n=int(input("enter the size of first list:"))
# i=0
# while i<n:
#     print("enter the element{}:".format(i+1))
#     l=int(input())
#     i+=1
#     list1.append(l)
# list2=[]
# i=0
# while i<n:
#     print("enter the element{}:".format(i+1))
#     l=int(input())
#     i+=1
#     list2.append(l)
# list3=[]
# k=0
# while k<n:
#     if list1[k] in list2:
#         list3.append(list1[k])
#     k+=1    
# print(list1)
# print(list2)
# print("common elements are :",list3)         
#program to convert a decimal number to binary,octal and hexadecimal

#decimal=input("enter the decimal number:")

#program to find factorial of a number

# num=int(input("enter the number:"))
# def fact():
#     if num==0:
#         print("factorial of 0 is 1")
#     elif(num<0):
#         print("factorial of negative number is not posible")
#     else:    
#        result=1
#        for i in range(1,num+1):
#         result=result*i
#        print("factorial is :",result)
# fact()    
# program to print febonacci series upto a limit
num=int(input("enter the range:"))
result=0
a=0
def sum(result):
    for i in range(0,num):
        a=result+i-1
        result=a
        print(result,end=",")
sum(result)
