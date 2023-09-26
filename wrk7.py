list=["anjaly","amalu","vismaya","arya","sandhya"]
print(list[2])
print("length of list is:",len(list))
for x in range(3,60,5):
    print(x)
for x in range(8):
    if(x==9):break
    print(x)
else:
    print("not print")    
for x in list:
    print(x)   
for x in "ar":
    print(x)     
for x in list:
    print(x) 
    if x=="vismaya":continue   
        

list2=[]
n=int(input("enter the size of list:"))
i=0
while i<n:
    print("enter the element{}:".format(i+1))
    l=str(input())
    i+=1
    list2.append(l)
    print(list2)
print("length is :",len(list2)) 
l1=[]
n1=int(input("enter the size of list:"))
i=0
while i<n1:
    print("enter the element{}:".format(i+1))
    l=int(input())
    l1.append(l)
    i+=1

l2=[]
j=0
while j<n1:
    print("enter the element{}:".format(j+1))
    l=int(input())
    l2.append(l)
    j+=1
k=0
l3=[]
while k<n1:
    if l1[k] in l2:
        l3.append(l1[k])
    k+=1
print(l1)
print(l2)
print(l3)

strg=str(input("enter the string:"))
reverse=''
count=len(strg)
while count>0:
    reverse+=strg[count-1]
    count=count-1
print("reverse of",strg ,"is")
print(reverse)
# program for finding greatest number
l4=[]
n1=int(input("enter the size of list:"))
i=0
while i<n1:
    print("enter the element{}:".format(i+1))
    l=int(input())
    l4.append(l)
    i+=1
l4.sort()
print("largest element is :",l4[n1-1])

# program for finding number of words in a string
string=[]
string=str(input("enter the words:"))
word=len(string.split())
print("number of words :",str(word))
# program for printing new list containing 5 characters\

l1=[]
n1=int(input("enter the size of list:"))
i=0
while i<n1:
    print("enter the list elements{}:".format(i+1))
    l=str(input())
    l1.append(l)
    i+=1
l2=[]    
for words in l1:
     if len(words) > 5:
        continue
     l2.append(words)
print(l2)    
# program for number pyramid

rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i+1): 
        print(j+1,end= "")
    print("\n")              
# program for alphabet pyramid

rows = int(input("Enter number of rows: "))
ascii=65
for i in range(rows):
    for j in range(i+1): 
         value=chr(ascii)
         print(value,end= "")
         ascii+=1 
    print("\n") 
# program for alphabet pyramid

rows = int(input("Enter number of rows: "))
ascii=65
for i in range(rows):
    for j in range(i+1): 
         value=chr(ascii)
         print(value,end= "")
    ascii+=1 
    print("\n")   
# program for printing even number pyramid

rows = int(input("Enter number of rows: "))
for i in range(rows):
    for j in range((i*2)+1): 
        print((i+1+j)*2,end="")
    print("\n")

    