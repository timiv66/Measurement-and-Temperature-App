#Mes functions
def incToFeet(inc):
    inc = float(inc)
    feet = inc /12.0
    return round(feet,2)

def feetToInc(feet):
    feet = float(feet)
    inc = feet * 12.0
    return round(inc,2)

def incToMile(inc):
    inc = float(inc)
    mile = inc / 63360
    return round(mile,2)

def mileToInc(mile):
    mile = float(mile)
    inc = mile * 63360
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

#Liquid functions
def galToOz(gal):
    gal = float(gal)
    oz = gal * 128
    return round(oz,2)

def ozToGal(oz):
    oz = float(oz)
    gal = oz/128
    return round(gal,2)

def galToCup(gal):
    gal = float(gal)
    cup = gal * 15.773
    return round(cup,2)

def cupToGal(cup):
    cup = float(cup)
    gal = cup/15.773
    return round(gal,2)

count = 0
while (count < 1):
    print("Hello welcome to Measurment and Temperature Converter!!!")
    mode = input("Enter 'mes' for measurment \nEnter 'temp' for temperature \nEnter 'liq' for liquids \n")

    #Measurment mode
    if (mode == "mes"):
        #Options
        print("\n1) Inches to feet")
        print("2) Feet to inches")
        print("3) Inches to miles")
        print("4) Miles to inches")
        print("5) Feet to miles")
        print("6) Miles to feet")
        mesChoice = input("Please select the conversion: ")
        
        
        #Inches to feet
        if (mesChoice == str(1)):
            inches = input("Enter the number of inches: ")
            feet = incToFeet(inches)
            print(str(inches) + " inches is equal to " + str(feet) + " feet\n")
            
            
        #Feet to inches
        elif(mesChoice == str(2)):
           feet = input("Enter the number of feet: ")
           inches = feetToInc(feet)
           print(str(feet) + " feet is equal to " + str(inches) + " inches")
           print("")
         
        #Inches to miles
        elif(mesChoice == str(3)):
            inc = input("Enter the number of inches: ")
            mile = incToMile(inc)
            print(str(inc) + " inches is equal to " + str(mile) + " miles")
            print("")
            
        #Miles to inches
        elif(mesChoice == str(4)):
            mile = input("Enter the number of miles: ")
            inc = mileToInc(mile)
            print(str(mile) + " miles is equal to " + str(inc) + " inches")
            print("")   
            
    #Temperature mode
    elif(mode == "temp"):
        #Options
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
            print(str(value) + " celsius is equal to " + str(fahren) + " fahrenheit\n")

        #Exit Program
        ans = input("Would you like to exit the program (Y/N): ")   
        if(ans == str("Y")):
            count = count + 1
            
    #Liquid Mode
    elif(mode =="liq"):
        #Options
        print("\n1)Gallon to ounce")
        print("2)Ounce to gallon")
        print("3)Gallon to cup")
        print("4)Cup to gallon")
        liqChoice = input("Please select the conversion: ")

        #Gallon to ounce
        if(liqChoice == str(1)):
            gal = input("Enter number of gallons: ")
            oz = galToOz(gal)
            print(str(gal) + " gallons is equal to " + str(oz) + " fluid ounces\n")

        #Ounce to gallon
        elif(liqChoice == str(2)):
            oz = input("Enter number of ounces: ")
            gal = ozToGal(oz)
            print(str(oz) + " fluid ounces is equal to " + str(gal) + " gallons\n")   

        #Gallon to cup
        if(liqChoice == str(3)):
            gal = input("Enter number of gallons: ")    
            cup = galToCup(gal)
            print(str(gal) + " gallons is equal to " + str(cup) + " cups\n")

        #Cup to gallon
        if(liqChoice == str(4)):
            cup = input("Enter number of cups: ")    
            gal = cupToGal(cup)
            print(str(cup) + " cups is equal to " + str(gal) + " gallons\n")

        #Exit Program
        ans = input("Would you like to exit the program (Y/N): ")   
        if(ans == str("Y")):
            count = count + 1