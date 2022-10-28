num = int(input('Enter Number Of File: '))
choice = int(input('Endless(1) Or End(2): '))
print('Be Careful On Potato PC If Your Using Endless Method!!!')
name = input('Input Name Of File: ')
message = input('Input Message In File: ')
if(choice==1):
    while(num>0):
        num += 1
        file = open(f'{name}{num}.txt', 'a')
        file.write(message)
        file.close
elif(choice==2):
    while(num>0):
        num -= 1
        file = open(f'{name}{num}.txt', 'a')
        file.write(message)
        file.close
else:
    print('There Is No Choice Like This!')
