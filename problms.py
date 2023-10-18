# num=[2,4,5]
# n=len(num)
# target=6
# for i in range(n):
#     for j in range(0,n):
#         if (num[i]+num[j]==target):
#             print([i,j]) 
#             break

#program to find the squareroot of a number
# num=int(input("enter a number:"))
# import  math
# x=math.sqrt(num)
# print("square root is:",x)

# program to print the number of words in a list
# list2=[]
# list2=str(input("enter the sentence:"))
# n=len(list2.split())
# print("number of words :",str(n))
   
# program to print longest word in the sentence
# list=[]
# list=str(input("enter the sentence:"))
# c=list.split()
# n=len(c)
# l2=[]  
# for words in list:
#      if n> 5:
#         continue
#      l2.append(words)
# print(c)  

# program to print words only starting with upper character

# string=[]
# string=str(input("enter the sentence:"))
# list2=[]

#       list2.append(p)
#       print(list2)

# import random
# l=[1,3,5,7,9]
# m=random.choice(l)
# print(m)

# rock,paper and scissors

# choice=['rock','paper','scissors']
# p=input("[rock,paper,scissors] enter your choice:")
# import random
# m=random.choice(choice)
# print(m)
# if p==m:
#     print("it's a tie")
# elif (p==choice[0] and m==choice[1]):
#       print("computer is the winner")    
# elif (p==choice[0] and m==choice[2]):
#      print("you win")      
# elif (p==choice[1] and m==choice[0]):
#      print("you wins")  
# elif (p==choice[1] and m==choice[2]):
#      print("computer is the winner")  
# elif (p==choice[2] and m==choice[0]):
#      print("computer is the winner")
# elif (p==choice[2] and m==choice[1]):
#      print("you wins") 
# else:
#      print("invalid input")    

# word guessing problem

# words=['parrot','duck','cat','dog','chicken','cow']
# import random
# m=random.choice(words)
# for i in m:
#     print("_",end=" ")
# guessed_letters=''
# chance=6
# while chance>0:
#     attempt=0
#     user_input=input("enter the guess:")
#     guessed_letters+=user_input
#     for x in m:
#         if x in guessed_letters:
#             print(x,end=" ")
#         else:
#             attempt+=1
#             print("_",end=" ")  
#     if attempt==0:
#         print("correct congratulations")                 
#     if user_input not in m:
#         chance-=1
#         print("wrong","\n","you have",chance,"chance")
#         if chance==0:
#             print("you loose")

# python program for password validation
# import re
# password=input("Enter your PASSWORD:")
# counter=''
# if len(password)>=8:
#    char = re.search("[a-z]", password)
#    if char:
#        char = re.search("[A-Z]", password)
#        if char:
#            char = re.search("[0-9]", password)
#            if char:
#                 char = re.search(r"[()!@$#%^&*+-,.?/\:;(){}\<>]", password)
#                 if char:
#                     print("valid password")
#                 else:
#                       print("password must contain atleast one special character:@#$%^&*-_")  
#            else:
#                print("password must contain atleast one digit")  
#        else:
#              print("password must contain capital letters")   
#    else:
#          print("password must contain lower case letters")                        
# else:
#     print("invalid password","\n"," password must have 8 characters")  

# find median of sorted list  
w=[20,22,23,23,24]
n=len(w)
k=int(n/2)
c=int(n/2)
m=(w[c]+w[c-1])/2
if n%2==1:
    print("Median is ",w[k])
else:
   print(m)