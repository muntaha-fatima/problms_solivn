def reverse_string(s):
 reversed_string =s[::-1]
 return reversed_string
user_input =   str(input('enter your name: '))

print("reverse string is: ",reverse_string(user_input))


def count_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}  
    count = sum(1 for five in s.lower() if five in vowels) 
    return count
user_input = input("Enter your word: ")  

print("Count of vowels is:", count_vowels(user_input))  



def product_of_digits(n):
  return sum(int(digit) for digit in str(n))
user_input=   int(input('enter your number: '))
print("sum of digit is:",product_of_digits(user_input)) 
