
def function_name(a, b, c, e):
    #print(a, b, c, e)
    return a+b+c+e




print( function_name(1, 2, 3, 4) )


def add_fun(a, b):
    c = a + b
    return c

def len_list(a):
    return len(a)


sum = add_fun(10, 10)
print(sum)


list_a = [1, 2, 3, 4]
print( len_list(list_a) )


sumPsum = 0
def pow(a):
    return a*a

for i in range(1,10):
    pSum = add_fun(pow(i), pow(i))
    sumPsum = sumPsum + pSum
print(sumPsum)



def return2(a):
    return a*a, a*a*a

r1, r2 = return2(10)
print(r1, r2)


def return3(a):
    return a*a, a*a*a, 10

a, _, _ = return3(10)
print(a,b)




