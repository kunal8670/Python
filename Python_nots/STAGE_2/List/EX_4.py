celsius = [0, 20, 37, 100]

fahrenheit = [(temp * 9/5) + 32 for temp in celsius]

print("Fahrenheit:", fahrenheit)  # [32.0, 68.0, 98.6, 212.0]
