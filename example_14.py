# # QUESTION: how "big" is `systems`? how many elements does it contain?
# # QUESTION: how many elements does it *conceptually* contain?
# systems = 'sequoia,vulcan,quartz,zin,sierra'
# print(f'{len(systems) = }')

# systems = systems.split(',')
# print(f'{len(systems) = }')


# # GIVEN: `reversed` allows you to loop over something in reverse
# # QUESTION|HARD: what is a requirement of the data you are looping over?
# systems = 'sequoia,vulcan,quartz,zin,sierra'.split(',')
# for s in reversed(systems):
#     print(f'{s = }')

# GIVEN: `enumerate` allows you to loop over a collection and its index
# QUESTION: what does the `start` parameter do?
# systems = 'sequoia,vulcan,quartz,zin,sierra'.split(',')
# for idx, s in enumerate(systems[3:], start=1):
#     print(f'{idx = }, {s = }')

# GIVEN: `enumerate` allows you to loop over a collection and its index
# QUESTION: what does the `start` parameter do?
#   ANSWER: it sets the index of where you start counting (but it does not
#           alter which elements you loop over)

# # `enumerate` is roughly equivalent to:
# def enumerate(xs, start=0):
#     return zip(range(start, len(xs) + start), xs)

# GIVEN: `zip` allows you to line up two or more pieces of data to loop
#        over together
# QUESTION: what if one of the collections is shorter than the other?
# systems = 'sequoia,vulcan,quartz,zin,sierra'.split(',')
# flops   = '20      5       3    .970   125    4627 271'.split()
# for s, f in zip(systems, flops):
#     print(f'{s = :>8}, {f = :>5}')

# xs = {1, 2, 3, 4, 5, 6, 7}
# for x in sorted(xs, reverse=True):
#     print(f'{x = }')


# QUESTION: what is the difference between `sorted(xs)` and `xs.sort()`
#           for a list?
# xs = [8, 3, 5, 2, 1]
# print(f'{xs = }')

# sorted_xs = sorted(xs)
# print(f'{sorted_xs = }')
# print(f'** {xs = } **')

# xs.sort()
# print(f'{xs = }')
#     

# we have seen `sum` and `len` before...
# xs = [1, 2, 3, 4, 5]
# print(f'{sum(xs) = }')
# print(f'{len(xs) = }')

# # `sum` can take a second argument, which is the initial value to start with
# print(f'{sum([], 1) = }')


# print(f'{sum([[1, 2, 3], [4, 5, 6]], []) = }')


# # QUESTION: why doesn't this work?

# print(f'{sum(["abc", "def", "xyz"], "") = }')


# # print(f'{sum(["abc", "def", "xyz"], "") = }') # bad
# print(f'{"".join(["abc", "def", "xyz"]) = }')   # good

# # we can guess what `min` and `max` do
# xs = [1, 2, 3, 4, 5]
# print(f'{min(xs) = }')
# print(f'{max(xs) = }')
# print(f'{max([], default=10) = }')

# # QUESTION: what does the `key` argument on `min`, `max`, and `sorted` do?
# xs = [1, 2, 3, 4, 5, -10, -20, -30, -40, -50]
# print(f'{min(xs) = } {min(xs, key=abs) = }')
# print(f'{max(xs) = } {max(xs, key=abs) = }')

# print(f'{sorted(xs)          = }')
# print(f'{sorted(xs, key=abs) = }')

# # we often want to build a list by looping over another list
# xs = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# ys = []
# for x in xs:
#     if x % 2 == 0:
#         ys.append(x ** 2)
# print(f'{xs = }')
# print(f'{ys = }')


# using comprehension syntax, we can rewrite the above…

# xs = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# ys = [x ** 2 for x in xs if x % 2 == 0]
# print(f'{xs = }')
# print(f'{ys = }')

# we have list, set, and dict comprehensions
# QUESTION: what do the following return?
# xs = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# ys = [x ** 2 for x in xs]
# zs = {x ** 2 for x in xs}
# ws = {x: x ** 2 for x in xs}
# ts = (x ** 2 for x in xs) # QUESTION: what is this?
# print(f'{xs = }')
# print(f'{ys = }')
# print(f'{zs = }')
# print(f'{ws = }')
# print(f'{ts = }')

# QUESTION|HARD: why isn't there an easy syntax
#                for a tuple comprehension?

# # we have list, set, and dict comprehensions
# # QUESTION: what do the following return?
# xs = [-4, -3, -2, -1, 0, 1, 2, 3, 4] # a `list`
# ys = [x ** 2 for x in xs] # a `list` with the squares
# zs = {x ** 2 for x in xs} # a `set` with the squares
# ws = {x: x ** 2 for x in xs} # a `dict` mapping values to their squares
# # ts = (x ** 2 for x in xs) # QUESTION: what is this?
#                             #   ANSWER: a generator expression

# # QUESTION|HARD: why isn't there an easy syntax
# #                for a tuple comprehension?
# #        ANSWER: a tuple typically represents a record, so
# #                it's unlikely to be constructed by a `for`-loop-based
# #                syntax

# # NOTE: using PEP-448—Additional Unpacking Generalizations…
# ts = *(x ** 2 for x in xs),

# TASK: use comprehension syntax to construct a lookup for
#       only the systems running RHEL.
#       - the key should be the system name
#       - the value should be the total nodes
#       e.g., {'sierra': 190_080, ...}
systems        = 'sierra,catalyst,lassen'.split(',')
os             = 'rhel,toss,rhel'.split(',')
nodes          = [4_320, 324, 684]
cores_per_node = [   44,  24,  44]
