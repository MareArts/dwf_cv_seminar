



#if + for
for i in range(1,10):
    if (i%2) == 0:
        print(i)


#cintinue & break
for i in range(1, 10):
    if (i%2) == 1:
        continue
    print(i)


for i in range(1, 100000):
    if i>=10:
        break
    if i%2 == 1:
        continue
    print(i)



for i in range(1,9):
    print(i)
    
    for j in range(1, 9):
        if (j%2)==0:
            continue

        print('{}*{}={}'.format(i,j,i*j))

    print('')




