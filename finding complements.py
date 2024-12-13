
n = int(input("Enter the number you want to find 1's & 2's complement: "))

b = bin(n)[2:]

ones_com = ""

for i in b:
    if i == '0':
        ones_com += '1'
    else:
        ones_com += '0'


twos_com = bin(int(ones_com,2) + 1) [2:] # 2 is the base of binary

print(b, "is the binary form of ",n)
print(ones_com,"is the 1's complement of", b)
print(f"The 2's complement is {twos_com} ")