mark=float(input("enter your mark percentage:"))
if(mark>=90 and mark<=100):
    print("A")
elif(mark<=89 and mark>=70):
        print("B")  
elif(mark<=79 and mark>=60):
     print("C") 
elif(mark<=59 and mark>=50):
     print("D")        
elif(mark<=49 and mark>=0):
     print("E")     
else:
    print("invalid input")    