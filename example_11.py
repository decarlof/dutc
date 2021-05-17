users = [
    # name   is_superuser  quota    username  systems-they-can-access
    ('alice',  True,      10_000,   'alice',  ['sierra', 'vulcan', 'quartz']),
    ('bob',    True,      20_000,   'bob0',   ['vulcan', 'quartz']),
]

# name, is_superuser, quota, username, systems = users[0]
# print(f'{name} can use {systems}')

for name, _, quota, _, systems in users:
    print(f'{name} has a quota of {quota // 1024} GiB on systems {systems}')
