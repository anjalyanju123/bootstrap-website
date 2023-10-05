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
# num=int(input("enter the range:"))
# result=0
# a=1
# def sum(result):
#     for i in range(0,num):
#         b=result+a

#         print(end=",")
# sum(result)

# program to convert decimal to binay,octal and hexadecimal
# a=0
# b=0
# c=0
# def convertion(a,b,c):
#     num=int(input("enter the number:"))
#     a=bin(num)
#     b=oct(num)
#     c=hex(num)
#     print("binary value of",num ,"is",a)  
#     print("octal value of",num ,"is",b)  
#     print("hexadecimal value of",num ,"is",c)  
# convertion(a,b,c)  

# program to sort a list
# list=[]
# n=int(input("enter the size of first list:"))
# i=0
# while i<n:
#     print("enter the element{}:".format(i+1))
#     l=int(input())
#     i+=1
#     list.append(l)   
# print("list before sorting:",list)
# def sort(list):
#     list.sort()
#     d=sorted(list)
#     print("after sorting",d)
# sort(list)     

# program to print pyramid pattern
c=int(input("enter the number of rows:"))
for i in range(c):
    print("* "*(i+1))
    for j in range(1,i+2):
        if j%2==0:
            for j in range(j,0,-1):
                 print(j,end=" ")
        print(j,end=" ")
    print()    