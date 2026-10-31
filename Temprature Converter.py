def tempratureConverter(temp, unit):
    if unit == "C":
        converted_temp = (temp * 9/5) + 32
        return f"{temp}°C is equal to {converted_temp}°F"
    elif unit == "F":
        converted_temp = (temp - 32) * 5 / 9
        return f"{temp}°F is equal to {converted_temp}°C"
    
temperature = float(input("Enter the temperature: "))
unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ")

result = tempratureConverter(temperature, unit)
print(result)