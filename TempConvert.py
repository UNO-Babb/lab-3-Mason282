#TempConvert.py
#Name:Mason Rodgers
#Date:2/7/25
#Assignment:TempConvert


def main():
  #Prompt the user for a Fahrenheit temperature
  #Convert that temperature to celsius, rounding to 1 decimal percision
  #Output converted temperature.
  print = input ("What do you want to convert to celsius?")
def fahrenheit_to_celsius(tempF):
  tempC = (tempF - 32) * (5/9)
  return round(tempC, 1)
def main():
    tempF = input("Enter temperature in Fahrenheit: ")
    tempF= float(tempF)
    tempC = fahrenheit_to_celsius(tempF)
    print(tempF, "degrees Fahrenheit is", tempC, "degrees Celsius")




if __name__ == '__main__':
  main()
