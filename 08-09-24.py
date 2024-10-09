# 1.Write a program which will find all such numbers which are divisible by 7 but are not a 
# multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be 
# printed in a comma-separated sequence on a single line.
li = []
for i in range(2000,3201):
    if i%7==0 and i%5!=0:
        li.append(str(i))
print(li)
 
# 2.With a given integral number n, write a program to generate a dictionary that contains (i, 
# i*i) such that is an integral number between 1 and n (both included). and then the program 
# should print the dictionary. Suppose the following input is supplied to the program: 8 Then, 
# the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
num = 6
dic = {}
for i in range(1,num+1):
    dic[i] = i*i
print(dic)

# # 3.Write a program which accepts a sequence of comma-separated numbers from console 
# # and generate a list and a tuple which contains every number. Suppose the following input 
# # is supplied to the program: 34,67,55,33,12,98 Then, the output should be: ['34', '67', '55', 
# # '33', '12', '98'] ('34', '67', '55', '33', '12', '98')
inpu = "1,2,3,4,5,6"
l = list(inpu.split(","))
t =tuple(inpu.split(","))
print(l)
print(t)


# # 4.Write a program that accepts a comma separated sequence of words as input and prints 
# # the words ina comma-separated sequence after sorting them alphabetically. Suppose the 
# # following input is supplied to the program: without, hello, bag, world Then, the output 
# # should be: bag,hello,without,world
inp = "without,hello,bag,world then"
inpu = inp.split(",")
print(inpu)
order = sorted(inpu)
print(",".join(order))


# # 5.Write a program that accepts a sentence and calculate the number of letters and digits. 
# # Suppose the following input is supplied to the program: hello world! 123 Then, the output 
# # should be: LETTERS 10 DIGITS 3
a = "hello worls! 123"
letters = 0
digits = 0
for i in range(len(a)):
    if a[i].isalpha:
        letters = letters+1
    elif a[i].isdigit:
        digits = digits+1
print(f"LETTERS {letters} DIGITS {digits}")


# # 6.Write a program that accepts a sentence and calculate the number of upper case letters 
# # and lower case letters. Suppose the following input is supplied to the program: Hello 
# # world! Then, the output should be: UPPER CASE 1 LOWER CASE 9
b = "Saqlain shaik MOHAMMAD"
upper = 0
lower = 0
for i in range(len(b)):
    if (b[i].isupper()):
        upper = upper+1
    elif (b[i].islower()):
        lower = lower+1
print(f"UPPER CASE {upper} LOWER CASE {lower}")

 
# # 7.Write a program that computes the net amount of a bank account based a transaction 
# # log from console input.The transaction log format is shown as following: D 100 W 200 D 
# # means deposit while W means withdrawal. Suppose the following input is supplied to the
# # program: D 300 D 300 W 200 D 100 Then, the output should be: 500
total = 0
while True:
    deposit_withdraw_transac = int(input())
    if deposit_withdraw_transac == "":
        break
    else:
        deposit_withdraw_transac = deposit_withdraw_transac.split(" ")
        if deposit_withdraw_transac[0] == "D":
            total = total + int(deposit_withdraw_transac[1])
        elif deposit_withdraw_transac[0] == "W":
            total = total - int(deposit_withdraw_transac[1])
print(total)
 