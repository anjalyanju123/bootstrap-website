n=int(input("enter the number of rows:"))
i=1
while i<=n:
    j=1
    while j<=i:
      print("*",end=" ")
      j+=1
    print()  
    i+=1
# using for loop
c=int(input("enter the number of rows:"))
for i in range(c):
    print("*"*(i+1))

def add(a,b):
    sum=a+b
    print(sum)
add(6,9) 

a=int(input("enter first digit:"))
b=int(input("enter second digit:"))
def add(a,b):
    sum=a+b
    return sum
print("sum is :",add(a,b))
  #program for counting vowels in a string

string=str(input("enter the string:")).lower() 
vowels=["a","e","i","o","u"]
count=0
for i in string:
    if i in vowels:
        count=count+1
print(count)    

