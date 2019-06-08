prime = []
composite = []
isComposite = False

while True:
    command = input()
    if command == "stop":
        break
    command_int = int(command)
    if command_int < 0:
        print('Number is negative.')
    elif command_int > 1:
        for check in range(2, command_int):
            if command_int % check == 0:
                isComposite = True
                break
            else:
                isComposite = False
        if isComposite:
            composite.append(command_int)
        else:
            prime.append(command_int)
    elif command_int == 1:
        composite.append(command_int)

print(f'Sum of all prime numbers is: {sum(prime)}')
print(f'Sum of all non prime numbers is: {sum(composite)}')


