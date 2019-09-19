result_1 = input()
result_2 = input()
result_3 = input()

win = 0
lose = 0
even = 0

if int(result_1[0]) > int(result_1[2]):
    win += 1
elif int(result_1[0]) < int(result_1[2]):
    lose += 1
elif int(result_1[0]) == int(result_1[2]):
    even += 1

if int(result_2[0]) > int(result_2[2]):
    win += 1
elif int(result_2[0]) < int(result_2[2]):
    lose += 1
elif int(result_2[0]) == int(result_2[2]):
    even += 1

if int(result_3[0]) > int(result_3[2]):
    win += 1
elif int(result_3[0]) < int(result_3[2]):
    lose += 1
elif int(result_3[0]) == int(result_3[2]):
    even += 1

print(f'Team won {win} games.')
print(f'Team lost {lose} games.')
print(f'Drawn games: {even}')