a = 5
b = 5.5
c = "str"
d = [5, 7, 9, "str", 5.5, [1 ,2]]
f = {5, 5, 5}

print(f'a = {a}')
print(d)

addition = a + 5
print(f'addition = {addition}')
subtraction = a - 5
print(f'subtraction = {subtraction}')
remainder1 = a % 3
print(f'remainder = {remainder1}')
z = a // 5
print(f'integer = {z}')
y = a / 5
print(f'float = {y}')
power = a ** 2
print(f'power = {power}')

mylist = (1, 2, 3, 4)
extended_mylist = mylist * 2
print(f'list multiplication: {extended_mylist}')

double_extended_list = mylist + extended_mylist
print(f'list addition: {double_extended_list}')

mylist_1 = [1, 5, 10, 20]
str_2 = ""

for j in range(len(mylist_1)):
    if mylist_1[j] % 2 == 0:
        if j != len(mylist_1) - 1:
            str_2 = str_2 + f'{mylist_1[j]},' # mylist_3 += f'{mylist_1[j]},'
        else:
            str_2 += f'{mylist_1[j]}'

print(str_2)

str_3 = "1,4,9,"

for j in str_3:
    print(j)

print(str_3[:len(str_3) - 1])

# print(','.join(map(lambda even: f'{even}', filter(lambda x: x % 2 == 0, mylist_1))))
print(','.join(map(str, filter(lambda x: x % 2 == 0, mylist_1))))

aa = 5
while aa != 1:
    aa -= 1 # aa = aa - 1

print(f'aa = {aa}')