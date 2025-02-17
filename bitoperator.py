num1 = 18
num2 = 7

print("AND operator: ", num1 & num2)
print("OR operator: ", num1 | num2)
print("XOR operator: ", num1 ^ num2)
print("NOT operator: ", ~num1)
print("RSHIFT operator: ", num1 >> num2)
print("LSHIFT operator: ", num1 << num2)

#Odd-Even using Bitwise operator

def oddeven(n):
    if (n^1 == n+1):
        print("It is an even number")
    else:
        print("It is an odd number")

n = int(input("Enter your number: "))
oddeven(n)

#Number of bits

def bits(n):
    count = 0
    while(n):
        count += 1
        n >>= 1
    return count

n = int(input("Enter your desired number"))
print("The total number of bits are: ", bits(n))