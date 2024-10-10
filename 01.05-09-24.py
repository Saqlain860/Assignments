# 1.Write a program that prints the numbers from 1 to 100. 
# For multiples of three, print "Fizz" instead of the number, and for multiples of five, print "Buzz". 
# For numbers which are multiples of both three and five, print "FizzBuzz".
for i in range(1,100):
    if(i%3==0):
        print("Fizz",end=",")
    elif(i%5==0):
        print("Buzz",end=",")
    elif(i%3==0 and i%5==0):
        print("FizzBuzz",end=",")
    else:
        print(i,end=",")
print(end="\n")


# 2.Write a program that checks if a number is prime. A prime number is a number greater than 1 that
#  is only divisible by 1 and itself.
print("--------------------------------------------------------------------------------------------")
num = 7
count = 0
if num<1:
    print("Enter a valid number")
else:
    for i in range(1,num+1):
        if(num%i==0):
            count+=1
    if(count==2):
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")


# 3.Write a program to check if a string is a palindrome. A palindrome is a word, phrase, or sequence 
# that reads the same forward and backward.
print("--------------------------------------------------------------------------------------------")
s = "madam"
s1 = " "
for ch in s:
    s1 = s[::-1]
if s == s1:
    print(f"{s} is a palindrom")
else:
    print(f"{s} is not a palindrom")


# 4.Write a program that generates a random number between 1 and 100, and asks the user to guess it. 
# The program should give hints ("too high" or "too low") until the user guesses correctly.
print("--------------------------------------------------------------------------------------------")
import random
number = random.randint(1,100)
user_number = 20  # or int(input("guess the numbre: "))
print(number)
if (user_number<number):
    print("too low")
elif user_number>number:
    print("too heigh")
elif user_number==number:
    print("congrasulations....")

 
# 5.Write a program that takes a number as input and prints the sum of its digits.
print("--------------------------------------------------------------------------------------------")
num2 = 1234
sum = 0
for i in str(num2):
        sum+=int(i)
print(sum)
 
# 6.Write a program to calculate the factorial of a number using a for loop.
print("--------------------------------------------------------------------------------------------")
num3 = 10
produ = 1
for i in range(1,num3+1):
    produ*=i
print(produ)
 

# 7.Write a program to find the largest of three numbers using if statements.
print("--------------------------------------------------------------------------------------------")
x = 90
y = 123
z = 90
largest = x
if(y>largest):
    largest = y
if(z>largest):
    largest = z
print(f"The largest number along three is {largest}")

 
# 8.Write a program to check if a number is an Armstrong number. An Armstrong number is a number that 
# is equal to the sum of its own digits raised to the power of the number of digits.
print("--------------------------------------------------------------------------------------------")
number = 153
add = 0
num4 = str(number)
length = int(len(num4))
mul = 1
for i in num4:
    mul=int(i)**length
    add +=mul
if(number==add):
    print(f"{number} is a armstrong number")
else:
    print(f"{number} is not a armstrong number")

 
# 9.Write a program that prints the multiplication table for a given number.
print("--------------------------------------------------------------------------------------------")
num9 = 5
for i in range(1,11):
    print(f"{num9} x {i} = {num9*i}")

 
# 10.Write a program that counts the number of even and odd numbers in a list.
print("--------------------------------------------------------------------------------------------")
l = [1,2,3,4,5,6,7,8,9]
even_count = 0
odd_count = 0
for i in l:
    if(i%2==0):
        even_count+=1
    else:
        odd_count+=1
print(f"Even numbers count is {even_count}")
print(f"Odd numbers count is {odd_count}")


 