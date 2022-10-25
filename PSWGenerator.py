import random
import string
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

lenght= int(input("How many letters would you like in your password?\n"))
# nr_letters= int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ''
password_1 = ''
password_2 = ''
password_3 = ''

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower + upper + num + symbols
temp = random.sample(all, lenght)
password = ''.join(temp)
print(password)

# for char in range (1, nr_letters + 1):
#     random_char = random.choice(letters)
#     password_1 += random_char
  
# for char in range (1, nr_symbols +1):
#     random_symb = random.choice(symbols)
#     password_2 += random_symb  
  
# for char in range(0, nr_numbers):
#     random_numb = random.choice(numbers)
#     password_3 += random_numb
  
