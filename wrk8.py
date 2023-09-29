# b="python"
# x = ""
# n=int(input("enter the number of rows:"))
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#       print("*",end=" ")
#       j+=1
#     print()  
#     i+=1
# using for loop
# c=int(input("enter the number of rows:"))
# for i in range(c):
#     print("*"*(i+1))

# def add(a,b):
#     sum=a+b
#     print(sum)
# add(6,9) 

# a=int(input("enter first digit:"))
# b=int(input("enter second digit:"))
# def add(a,b):
#     sum=a+b
#     return sum
# print("sum is :",add(a,b))
b="python"
n=len(b) 
i=0
while i<=n:
    j=0
    while j<=i-1:
      print(b[j],end=" ")
      j+=1      
    i+=1
    print()
i=0    
while i<=n:
  k=0
  while k<=n-i-1:
    print(b[k],end=" ")
    k+=1  
  i+=1
  print()     
