import random

print( random.random())

hum=int(input(“enter Humidity:”))
temp=int(input(“enter Temperature:”))

temp=temp*random.random()
hum=hum*random.random()

if hum>90:
       print(“Hazard”)
else:
       print(“Humidity is Normal”)

if temp>80:
       k=0
       while k<=10:
               print(“------High Temperature------“)
               k=k+1
elif temp<80:
        print(“Temperature is Normal”)
elif temp==80:
         print(“Temperature at max Level”)
