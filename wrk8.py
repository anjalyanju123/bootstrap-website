# b="python"
# x = ""
# n=5
# for i in b:
#     x += i
#     print(x)
# for i in range(n):
#     for j in range(i + 1):
#         print(b[:], end="")
#     print()
# for i in range(n-1):
#         for j in range(n - i - 1):
#          print(b[:j-i],end="")
#         print()

string= input("Enter string :")   
revstr="" 
for i in string: 
  revstr = i + revstr
# print("Reversed string : ",revstr) 
 
if(string==revstr): 
   print("The string is a palindrome.") 
else: 
   print("The string is not a palindrome.") 
