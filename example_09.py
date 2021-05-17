# this is a Python `list`
xs = [1, 2, 4, 8, 16, 32, 64]

# QUESTION: is the `list` heterogeneous or homogeneous?

# MULTIPLE-CHOICE:
#   - a heterogeneous container {CAN, CANNOT} contain objects of different types
#   - a homogeneous container {CAN, CANNOT} contain objects of different types

# QUESTION: what is the common case for a `list`?

# HINT:

# xs = [1, 2.0, True, 8+1j]
# for x in xs:
#     print(f'{x + 1 = }')

# xs = [1, 2.0, 'four', False, None, [1, 2, 3]]
# for x in xs:
#     print(f'{x = }')


# xs = [1, 2, 3, 4]
# xs.append(5)
# xs.append(6)
# xs.append(7)

# print(f'{xs = }')

# # while xs:
# #     print(f'{xs.pop() = }')
# #     print(f'{xs = }')


xs = [1, 2, 3]

if xs:
    print('xs is not empty')
else:
    print('xs is empty')
