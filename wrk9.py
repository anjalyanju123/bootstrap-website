# program for printing first letter of each word capitalized
# name=str(input("enter the name:"))
# def myname():
#   result = name.title()
#   return result
# print(myname())
# program to remove all special characters
sentence=str(input("enter the string:"))
def character():
 charts=""
 new_sentence=""
 for i in sentence:
     if i.isalpha():
      charts=i+charts
      new_sentence= charts.replace(i,"")
      print(new_sentence)
 print(character())   