celcius= float(input("Please enter the temperature in celcious: "))
print("\n your entered value is",celcius)
farenheit= (celcius * 1.8) +32
print('%0.1f degree celcius is equal to %0.1f degree farenheit' 
      %(celcius, farenheit))

temp=farenheit
if (temp>= 104):
    print("It's hot")
elif (temp <= 50):
   print("It's cold")
else:
   print("The temperature is nice")