# list=["anjaly","amalu","vismaya","arya","sandhya"]
# print(list[2])
# print("length of list is:",len(list))
# for x in range(3,60,5):
#     print(x)
# for x in range(8):
#     if(x==9):break
#     print(x)
# else:
#     print("not print")    
# for x in list:
#     print(x)   
# for x in "ar":
#     print(x)     
# for x in list:
#     print(x) 
#     if x=="vismaya":continue   
        

# list2=[]
# n=int(input("enter the size of list:"))
# i=0
# while i<n:
#     print("enter the element{}:".format(i+1))
#     l=str(input())
#     i+=1
#     list2.append(l)
#     print(list2)
# print("length is :",len(list2)) 
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