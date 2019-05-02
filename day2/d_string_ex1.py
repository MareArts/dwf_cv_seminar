
str_a = 'my'
str_b = 'name'
str_c = 'is'
str_d = 'leon'
str_e = str_a + str_b + str_c + str_d
print(str_e)

str_e = str_a + ' ' + str_b + ' ' + str_c + ' ' + str_d
print(str_e)

str_e = '{} {} {} {}'.format(str_a, str_b, str_c, str_d)
print(str_e)


print( len(str_e) )
print( str_e[3:5] )
print( str_e[:-4] )

word = str_e.split(' ')
print(word)

str_e = str_e.upper()
print(str_e)


