#Mes functions
def incToFeet(inc):
    inc = float(inc)
    feet = inc /12.0
    return round(feet,2)

def feetToInc(feet):
    feet = float(feet)
    inc = feet * 12.0
    return round(inc,2)

#Temp functions
def fahToCel(fah):
    fah = float(fah)
    cel = (fah - 32) * (5/9)
    return round(cel,2)

def celToFah(cel):
    cel = float(cel)
    fah = cel * (9/5) + 32
    return round(fah,2)

count = 0
while (count < 1):
    print("Hello welcome to Measurment and Temperature Converter!!!")
    mode = input("Enter 'mes' for measurment or 'temp' for temperature(Enter X to exit program): ")

    #Measurment mode
    if (mode == "mes"):
        print("")
        print("1) Inches to feet")
        print("2) Feet to inches")
        print("3) Inches to miles")
        print("4) Miles to inches")
        print("5) Feet to miles")
        print("6) Miles to feet")
        mesChoice = input("Please select the conversion: ")
        print("")
        
        #Inches to feet
        if (mesChoice == str(1)):
            inches = input("Enter the number of inches: ")
            feet = incToFeet(inches)
            print(str(inches) + " inches is equal to " + str(feet) + " feet")
            print("")
            
        #Feet to inches
        elif(mesChoice == str(2)):
           feet = input("Enter the number of feet: ")
           inches = feetToInc(feet)
           print(str(feet) + " feet is equal to " + str(inches) + " inches")
           print("")
           
            
    #Temperature mode
    elif(mode == "temp"):
        print("")
        print("1)Fahrenheit to celsius")
        print("2)Celsius to fahrenheit")
        tempChoice = input("Please select the conversion: ")
        print("")
        
        #Fahrenheit to celsius
        if(tempChoice == str(1)):
            value = input("Enter fahrenheit value: ")
            celsius = fahToCel(value)
            print(str(value) + " fahrenheit is equal to " + str(celsius) + " celsius")
            print("")   
            
        #Celsius to fahrenheit
        elif(tempChoice == str(2)):
            value = input("Enter celsius value: ")
            fahren = celToFah(value)
            print(str(value) + " celsius is equal to " + str(fahren) + " fahrenheit")
            print("")
            
        #Exit program
        elif(tempChoice == "X" | tempChoice == "x"): 
            count = count + 1
    elif(mode == "X"):
        count = count + 1
