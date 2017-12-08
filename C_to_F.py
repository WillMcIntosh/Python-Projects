def CtoF(temp_C):
    temp_F = (temp_C * 9/5) + 32
    return temp_F

user_temp = float(input("Enter a temperature in Celsius: "))

if user_temp < -273.15:
    print("Error! This temperature is literally impossible. Check yourself.")
else:
    print("In Fahrenheit, your temperature is ", CtoF(user_temp))
