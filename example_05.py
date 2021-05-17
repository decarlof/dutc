from random import randrange

kibi = 1024
mebi = 1024 ** 2
gibi = 1024 ** 3
tebi = 1024 ** 4
total_storage = 4 * tebi
current_storage = 0
day = 0

while True:
    added  = randrange(4 * gibi, 14 * gibi)
    removed = randrange(0 * gibi,  2 * gibi)
    if current_storage + added - removed > total_storage:
        print('Shut down the machine; users need to clean up their ~!')
        break
    current_storage += added - removed
    day += 1

print(f'{day = }')
print(f'{current_storage = :,d}')
print(f'{total_storage   = :,d}')