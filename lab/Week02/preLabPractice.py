def transform(f):
    result = (float(f) - 32) * 5 / 9
    
    return result

temp = input("Enter the temperature in Fahrenheit:")

result = transform(temp)

print('Celsius:',result)