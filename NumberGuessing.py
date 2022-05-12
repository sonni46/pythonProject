import random

pc = random.randint(1,50)
error = []
print(pc)

while True:
    user = int(input('Guess number between 1-50 '))
    error.append(user)
    if user < pc:
        print('to low')
    elif user > pc:
        print('to high')
    else:
        print('Good job')
        print(f'error {len(error)}')
        break
