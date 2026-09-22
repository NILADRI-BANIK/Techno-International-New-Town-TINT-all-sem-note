def decimal_to_binary(n):
    if n == 0:
        return '' 
    else:
        return decimal_to_binary(n // 2) + str(n % 2)  
n = int(input("Enter a decimal number to convert to binary: "))
if n < 0:
    print("Binary representation is not defined for negative numbers.")
elif n == 0:
    print("The binary equivalent of 0 is 0.")
else:
    binary = decimal_to_binary(n)
    print("The binary equivalent is ",binary)
