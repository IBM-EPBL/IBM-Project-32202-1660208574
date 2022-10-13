import random 
print(random.random()) 
humid=int(input("enter the Humidity:")) 
temp=int(input("enter the temperature:")) 
temp = temp*random.random() 
humid=humid*random.random() 
if humid>90:
    print("Hazard") 
else:
    print("Humidity is normal") 

if temp>80:
    k=0 
    while k<=10: 
        print("High Temperature") 
        k=k+1 
elif temp<80:
    print("Temperature is normal") 
elif temp==80:
    print("Temperature at maximum level")
