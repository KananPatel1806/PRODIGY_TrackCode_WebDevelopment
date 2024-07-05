def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return kelvin * 9/5 - 459.67
def convert_temperature():
    print("Temperature Conversion Program")
    print("-------------------------------")
    
    # Get user input
    temperature = float(input("Enter the temperature value: "))
    original_unit = input("Enter the original unit of measurement (Celsius, Fahrenheit, or Kelvin): ").strip().lower()
    
    # Perform conversions based on original unit
    if original_unit == 'celsius':
        celsius = temperature
        fahrenheit = celsius_to_fahrenheit(celsius)
        kelvin = celsius_to_kelvin(celsius)
    elif original_unit == 'fahrenheit':
        fahrenheit = temperature
        celsius = fahrenheit_to_celsius(fahrenheit)
        kelvin = fahrenheit_to_kelvin(fahrenheit)
    elif original_unit == 'kelvin':
        kelvin = temperature
        celsius = kelvin_to_celsius(kelvin)
        fahrenheit = kelvin_to_fahrenheit(kelvin)
    else:
        print("Invalid unit of measurement. Please enter Celsius, Fahrenheit, or Kelvin.")
        return
    
    # Display results
    print(f"Original Temperature: {temperature} {original_unit.capitalize()}")
    print(f"In Celsius: {celsius} Celsius")
    print(f"In Fahrenheit: {fahrenheit} Fahrenheit")
    print(f"In Kelvin: {kelvin} Kelvin")
if __name__ == "__main__":
    convert_temperature()




    
