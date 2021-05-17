# TASK: given the below timing, print out a performance
#       report listing how long each step took
#       e.g., start    -          pre-boot: 23 μs
#             pre-boot -              boot: 73 μs
#             boot     - filesystems ready: 86 μs

from datetime import datetime, timedelta
from random import randrange
from itertools import islice, tee

nwise = lambda g, n=2: zip(*(islice(g, i, None) for i, g in enumerate(tee(g, n))))

times = {
    'start':             (start := datetime.today()),
    'pre-boot':          start + timedelta(microseconds=  0 + randrange(10, 100)),
    'boot':              start + timedelta(microseconds=100 + randrange(10, 100)),
    'filesystems ready': start + timedelta(microseconds=200 + randrange(10, 100)),
    'os ready':          start + timedelta(microseconds=300 + randrange(10, 100)),
    'networking ready':  start + timedelta(microseconds=400 + randrange(10, 100)),
    'ready for use':     start + timedelta(microseconds=500 + randrange(10, 100)),
}

# print('Report I'.center(48, '-'))
# prev_ev, prev_tm = None, None
# for curr_ev, curr_tm in times.items():
#     if prev_ev is None:
#         prev_ev, prev_tm = curr_ev, curr_tm
#         continue
#     print(f'{prev_ev:<18} - {curr_ev:>18} {(curr_tm - prev_tm).total_seconds() * 1e6:>5.1f} \N{micro sign}s')
#     prev_ev, prev_tm = curr_ev, curr_tm

# print('Report I'.center(48, '-'))
# times = list(times.items())
# print(times)
# for idx in range(1, len(times)):
#     prev_ev, prev_tm = times[idx-1]
#     curr_ev, curr_tm = times[idx]
#     print(f'{prev_ev:<18} - {curr_ev:>18} {(curr_tm - prev_tm).total_seconds() * 1e6:>5.1f} \N{micro sign}s')

# def pairwise(xs):
#     xs = [*xs]
#     return zip(xs, xs[1:])

# print(times.items())

# print('Report I'.center(48, '-'))
# for (prev_ev, prev_tm), (curr_ev, curr_tm) in pairwise(times.items()):
#     print(f'{prev_ev:<18} - {curr_ev:>18} {(curr_tm - prev_tm).total_seconds() * 1e6:>5.1f} \N{micro sign}s')

# print('Report I'.center(48, '-'))
# for (prev_ev, prev_tm), (curr_ev, curr_tm) in nwise(times.items()):
#     print(f'{prev_ev:<18} - {curr_ev:>18} {(curr_tm - prev_tm).total_seconds() * 1e6:>5.1f} \N{micro sign}s')


# print('Report II'.center(57, '-'))
# times = list(times.items())
# prev_ev, prev_tm = times[0]
# print(f'{prev_ev:<18}...{"":>18} {"":5}    {prev_tm:%H:%M:%S}')
# for idx in range(1, len(times)):
#     prev_ev, prev_tm = times[idx-1]
#     curr_ev, curr_tm = times[idx]
#     print(f'{prev_ev:<18} - {curr_ev:>18} {(curr_tm - prev_tm).total_seconds() * 1e6:>5.1f} \N{micro sign}s {curr_tm:%H:%M:%S}')
# curr_ev, curr_tm = times[-1]
# print(f'{"":<18}...{curr_ev:>18} {"":5}    {curr_tm:%H:%M:%S}')

# 

from itertools import islice, tee, repeat, chain, repeat, zip_longest
nwise = lambda g, n=2: zip(*(islice(g, i, None) for i, g in enumerate(tee(g, n))))
nwise_longest = lambda g, n=2, fv=object(): zip_longest(*(islice(g, i, None) for i, g in enumerate(tee(g, n))), fillvalue=fv)
first = lambda g, n=1: zip(chain(repeat(True, n), repeat(False)), g)
last = lambda g, m=1, s=object(): ((y[-1] is s, x) for x, *y in nwise_longest(g, m+1, s))
first_and_last = lambda g, n=1, m=1: ((is_first, is_last, x) for is_first, (is_last, x) in first(last(g, m=m), n=n))

print('Report II'.center(57, '-'))
for is_first, is_last, ((prev_ev, prev_tm), (curr_ev, curr_tm)) in first_and_last(nwise(times.items())):
    if is_first:
        print(f'{prev_ev:<18}...{"":>18} {"":5}    {prev_tm:%H:%M:%S}')
    print(f'{prev_ev:<18} - {curr_ev:>18} {(curr_tm - prev_tm).total_seconds() * 1e6:>5.1f} \N{micro sign}s {curr_tm:%H:%M:%S}')
    if is_last:
        print(f'{"":<18}...{curr_ev:>18} {"":5}    {curr_tm:%H:%M:%S}')

        




