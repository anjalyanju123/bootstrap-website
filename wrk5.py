e=int(input("enter the month::"))
d={1:"january",2:"february",3:"march",4:"April",5:"May",6:"june",7:"july",8:"August",9:"september",10:"october",11:"november",12:"december"}
if(e==1):
    print(d[1],"31 days")
elif(e==2):
    print(d[2],"28 days")
elif(e==3):
    print(d[3],"31 days")    
elif(e==4):
    print(d[4],"30 days") 
elif(e==5):
    print(d[5],"31 days") 
elif(e==6):
    print(d[6],"30 days")            
elif(e==7):
    print(d[7],"31 days")   
elif(e==8):
    print(d[8],"31 days")    
elif(e==9):
    print(d[9],"30 days")      
elif(e==10):
    print(d[10],"31 days")  
elif(e==11):
    print(d[11],"30 days")            
elif(e==12):
    print(d[12],"31 days")         
else:
    print("invalid input")  


e=int(input("enter the number of days:"))
if(e==28):
    print("february")
elif(e==30):
    print("April,june,september,november")    
elif(e==31):
    print("January,march,may,july,August,october,december")    
else:
    print("invalid input")          

e=str(input("enter the month:"))
d={31:["January","march","may","july","August","october","december"],
   30:["April","june","september","november"],
   28:"february"}
if(e in d[31]):
    print("31 days")
elif(e in d[30]):
    print("30 days")
elif(e in d[28]):
    print("28 days")    
else:
    print("inavlid input")
