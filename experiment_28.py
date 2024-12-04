input_string = "Tom 25 Rahu22 2@$"

letters = filter(lambda x: x.isalpha(), input_string)  
uppercase_letters = list(map(lambda x: x.upper(), letters)) 
print("Uppercase Letters:", uppercase_letters)

digits = filter(lambda x: x.isdigit(), input_string)  
squared_digits = list(map(lambda x: int(x)**2, digits))  
print("Squared Digits:", squared_digits)

alphanumeric = filter(lambda x: x.isalnum(), input_string)  
alphanumeric_words = list(alphanumeric)  
print("Alphanumeric Characters:", alphanumeric_words)