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

# words=['parrot','duck','cat','dog','chicken']
# import random
# m=random.choice(words)
# n=len(m)
# for i in range(n):
#     print("_",end=" ")
# print()
# user_input=input("Guess the word(hint:animal name):")    
# chance=6
# i=1
# while i<=chance:
#   if m==user_input:
#     print("congratulations correct")     
#     for j in range(n):
#       if user_input in m:
#          print(user_input,end=" ")
#       else:
#          print("_")      
#     i+=1
    