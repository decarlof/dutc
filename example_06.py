from random import randrange

GiB = 1024 ** 3
TiB = 1024 ** 4
total_storage = 4 * TiB

users = [
    # name    day  add rem 
    ['alice',  [], [], [],],
    ['bob',    [],  [], [],],
    ['charlie',[],  [], [],],
    ['dana',   [],  [], [],],
]

for day in range(1_000_000):
    for u in users:
        u[-3].append( day)
        u[-2].append(  randrange(4 * GiB, 14 * GiB) )
        u[-1].append( -randrange(0 * GiB,  2 * GiB) )

    current_storage = 0
    for u in users:
        current_storage += sum(u[-2]) + sum(u[-1])
    if current_storage > total_storage:
        break
else:
    print("simulation didn't terminate")
print(f'{day = }')

max_adder   = [None, [],]
max_remover = [None, [],]
for u in users:
    if sum(u[-2]) > sum(max_adder[-1]):
        max_adder = u[0], u[-2]
    if sum(u[-1]) < sum(max_remover[-1]):
        max_remover = u[0], u[-1]
print(f'{max_adder[0]   = }, {sum(max_adder[-1])   = }')
print(f'{max_remover[0] = }, {sum(max_remover[-1]) = }')
