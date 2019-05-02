

a = input()
b = input()

a = int(a)
b = int(b)

print(a, b)

for i in range(1,a):
    for j in range(1,b):
        print('*', end='')
    print('')


for i in range(1,a):
    for j in range(1,i):
        print('*', end='')
    print('')




input 5
output #1
*****
****
***
**
*

output #2
*
**
***
****
*****

output #3
    *
   ***
  *****
 *******
*********

output #4
*********
 *******
  *****
   ***
    *

output #5
    *
   **
  ***
 ****
*****




# input 4, 3

# output #1
****
 ****
  ****
 ****
****

# output #2
****    ****
 ****  ****
  ********
 ****  ****
****    ****


# input 5, 3

# output #1
*****
 *****
  *****
 *****
*****

# output #2
*****    *****
 *****  *****
  **********
 ***** *****
*****   *****



