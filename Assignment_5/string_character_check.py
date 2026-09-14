# Program to check and count different types of characters in a string

text = input("Enter a string: ")

uppercase = []
lowercase = []
digits = []
special = []

for char in text:
    if 'A' <= char <= 'Z':
        uppercase.append(char)
    elif 'a' <= char <= 'z':
        lowercase.append(char)
    elif '0' <= char <= '9':
        digits.append(char)
    else:
        special.append(char)

print("\nUppercase characters:", uppercase)
print("Number of uppercase characters:", len(uppercase))

print("\nLowercase characters:", lowercase)
print("Number of lowercase characters:", len(lowercase))

print("\nDigits:", digits)
print("Number of digits:", len(digits))

print("\nSpecial characters:", special)
print("Number of special characters:", len(special))

# Check whether the string contains only A-Z, a-z and 0-9
if len(special) == 0:
    print("\nThe string contains only A-Z, a-z and 0-9 characters.")
else:
    print("\nThe string contains characters other than A-Z, a-z and 0-9.")
