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
# def febonacci(num):
#     a=0
#     b=1
#     c=0
#     print(a,end=" ")
#     for i in range(1,num):
#         a=b
#         b=c    
#         c=a+b
#         print(c,end=" ")
        
# if num<=0:
#     print("enter a positive integer!")
# else:
#     febonacci(num)

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
# c=int(input("enter the number of rows:"))
# for i in range(c):
#     print("* "*(i+1))   
#     if i%2==0:
#          for k in range(i+1,0,-1):
#                print(k,end=" ")
#     else:
#            for j in range(0,i+1):           
#               print(j+1,end=" ")
#            print()    
#     print()  

# program to print the pairs of numbers whose sum is equal to 18
# b=[3,8,12,7,6,10,21,15]
# n=len(b)
# for i in range(n):  
#         for j in range(i+1,n):
#           if (b[i]+b[j]==18):
#             print((b[i],b[j])) 
#             break
# program to find the the pairs of words in a list
# words=['apple','banana','cherry','date']
# newlist=[]
# n=len(words)
# for i in range(n):
#      for j in range(n):
#         for x in words[i]:
#           if x in words[j]:
#             pairs=(words[i],words[j])
#             newlist.append(pairs)
#             break
# print(newlist)

# program to print the pairs of number with its sum is odd and product is even
# b=[2,3,4,5,6]
# def find(sum):    
#   n=len(b)
#   for i in range(n):
#     for j in range(i+1,n):
#         sum=b[i]+b[j]
#         pdt=b[i]*b[j]
#         if((sum%2==1) and (pdt%2==0)):
#             print((b[i],b[j])) 
# find(sum)            
