# a `str` can be written to disk or to the network
#   by `.encode`ing it
# NOTE: the default encoding will change depending
#       on your operating and system setup
from sys import getdefaultencoding
print(f'{getdefaultencoding() = }')

# s = 'Lebron James'
# print(f'{len(b := s.encode("utf-8")) = }', f'{b = }', sep='\n', end='\n\n')
# print(f'{len(b := s.encode("latin-1")) = }', f'{b = }', sep='\n', end='\n\n')
# print(f'{len(b := s.encode("iso-8859-1")) = }', f'{b = }', sep='\n', end='\n\n')

# s = 'José Canseco'
# print(f'{len(s) = }', f'{s = }', sep='\n', end='\n\n')
# print(f'{len(b := s.encode("utf-8")) = }', f'{b = }', sep='\n', end='\n\n')
# print(f'{len(b := s.encode("latin-1")) = }', f'{b = }', sep='\n', end='\n\n')
# print(f'{len(b := s.encode("iso-8859-1")) = }', f'{b = }', sep='\n', end='\n\n')


# s = 'Fußball-Club Bayern München'
# print(f'{len(s) = }', f'{s = }', sep='\n', end='\n\n')
# print(f'{len(b := s.encode("utf-8")) = }', f'{b = }', sep='\n', end='\n\n')
# print(f'{len(b := s.encode("latin-1")) = }', f'{b = }', sep='\n', end='\n\n')
# print(f'{len(b := s.encode("iso-8859-1")) = }', f'{b = }', sep='\n', end='\n\n')


# s = '你好嗎'
# print(f'{len(s) = }', f'{s = }', sep='\n', end='\n\n')
# print(f'{len(b := s.encode("utf-8")) = }', f'{b = }', sep='\n', end='\n\n')

# QUESTION: why don't these work?
# print(f'{len(b := s.encode("latin-1")) = }', f'{b = }', sep='\n', end='\n\n')
# print(f'{len(b := s.encode("iso-8859-1")) = }', f'{b = }', sep='\n', end='\n\n')

# QUESTION: why don't these work?
#   ANSWER: some characters CANNOT be represented in some encodings
#           latin-1 and iso-8859-1 cannot represent non-Latin alphabets
#           (e.g., Chinese characters)


# the result of `.encode()` a string is a `bytes`
s = 'abcd'
b = s.encode()
assert type(s) is str   # NOTE: don't actually ever do this
assert type(b) is bytes # QUESTION|MEDIUM: why not?
assert isinstance(s, str)
assert isinstance(b, bytes)


# a `bytes` can be created using b'', b"", b'''''', b""""""
# a `bytes` can only contain values 0-255, encoded as ASCII
b = b'\0'
b = b"abc"
b = b"\n\1abc\255"
# b = b'abcdé' # INVALID! why?

# a `str` is a sequence; when you iterate over it, you get the individual
#   "characters" (strictly, Unicode code-points)
# s = 'abcdefghi'
# print(f'{s     = }')
# print(f'{s[2]  = }')
# print(f'{s[:3] = }')
# for c in 'abcdef':
#     print(c)

# a `bytes` is also a sequence; when you iterate over it, you get the individual
#   bytes
# b = 'abcdefghi'
# print(f'{b     = }')
# print(f'{b[2]  = }')
# print(f'{b[:3] = }')

# # QUESTION: why is the output below different than the above?
# for x in b'abcdef':
#     print(x)


# QUESTION: why is the output below different than the above?
#   ANSWER: when iterating over a `bytes`, you iterate over the
#           byte values (which are represented as `int` values 0 ≤ x < 256)

# NOTE: the builtin functions `ord` and `chr`
#       allow you to convert to/from a string/ordinal value
# x = '\n'
# print(f'{x      = }')
# print(f'{ord(x) = }')

# x = 0x2764
# print(f'{hex(x) = }')
# print(f'{chr(x) = }')


# # NOTE: you can encode Unicode characters by "name" in a Python string
# s = 'I \N{heavy black heart} Python' 
# print(f'{s = }')
# print(s.encode('utf-8'))

# # you can `.decode()` a `bytes` into a `str`
# b = b'I \xe2\x9d\xa4 Python'
# s = b.decode('utf-8')
# print(f'{b = }')
# print(f'{s = }')

# you can `.split` a `str` to a `list` of `str`
# you can `.join` a `list` (or other iterable) of `str` back into a single `str`
# sports = 'basketball,baseball,tennis'
# print(f'{sports = }')
# print(f'{sports.split(",") = }')

# sports = ['football', 'soccer', 'rugby']
# print(f'{sports = }')
# print(f'{", ".join(sports) = }')

# # NOTICE the reflectional symmetry
# 'a-b-c'.split('-')
# '-'.join(['a', 'b', 'c'])

# s = []
# for c in 'abcdefg':
#     s.append(c.upper())
# print(f'{"".join(s) = }')


# QUESTION: is a `str`/`bytes` mutable or immutable?

s = 'Lebron James'
print(f'{s = }')

s = s.replace('Lebron ', '')
s = s + ' Harden'
print(f'{s = }')
