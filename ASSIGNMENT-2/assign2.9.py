# Convert Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

c = float(input("Enter temperature in Celsius: "))
print(f"Temperature in Fahrenheit: {celsius_to_fahrenheit(c)}")
