list_a = ['a', 'bc', 'def']

print(list_a[0])
#a
print(list_a[1])
#bc
print(list_a[2])
#def
print(list_a[0:2])
#['a', 'bc']
print(list_a[0:])
#['a', 'bc', 'def']
print(list_a[1:])
#['bc', 'def']
print(list_a[:])
#['a', 'bc', 'def']
print(list_a[:-1])
#['a', 'bc']
print(list_a[:-2])
#['a']

#---------------------------------------------------------

list_b = [[1, 2, 3, 4, 10, 10], [5, 6, 7, 8]]
print(list_b[1][1])
#[1, 2, 3, 4]

print(list_b[0][:-1])
#[1, 2]

print(len(list_b))
#2
print(len(list_b[0]))
#4

