

list_a=[]
import random
while len(list_a) != 3:
    r=random.randint(1,9)
    if r not in list_a: list_a.append(r)
secret = list_a[0]+list_a[1]*10+list_a[2]*100
#print(secret)

# #game start
#stop when palyer tried 20 times !!
while(True):
    guess = input()
    guess = int(guess)

    #######
    #make code here!!
    print("ex) 2ball 2 strike")
    print("ex) 3out")
    #######

    if guess==secret:
        print('home run!!')
        break
