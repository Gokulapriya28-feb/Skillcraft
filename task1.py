print("Temperature between Celcius,Fharenheit, and Kelvin:")
print("1.Celcius to Fharenheit and Kelvin:")
print("2.Fharenheit to Celcius and kelvin:")
print("3.Kelvin to Celcius and FharenheitL")

choice=int(input("Enter the choice(1/2/3):"))

if(choice==1):
    c=float(input("Enter the temperature in Celcius:"))
    f=(c*9/5)+32
    k=c+273.15
    print("Fharenheit:",f)
    print("Kelvin:",k)

elif(choice==2):
    f=float(input("Enter the temperature in Fharenheit:"))
    c=(f-32)*5/9
    k=c+273.15
    print("Celcius:",c)
    print("Kelvin:",k)

elif (choice==3):
    k=float(input("Enter the temperature in kelvin:"))
    c=k-273.15
    f=(c*9/5)+32
    print("Celcius",c)
    print("Fharenheit:",f)
else:
    print("invalid choice")
    
