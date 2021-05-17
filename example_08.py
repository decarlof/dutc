from collections import Counter

# TASK: compute the word frequencies in the below text
#       and report on the three most common words that appear
text = '''
Searching and waiting, not wanting anything,
Loving and yearning, but losing everything.
Admiring the beauty, with my eyes being shot,
Perceive what no one saw, nobody knows it’s what,
Awed by the harmony, amazed by the secret,
Picturing in my mind, though have not seen it.
Adoring and loving everything that is clean,
The wind, white clouds, the snow and my dream;
To do what’s proper surely not for heaven,
Not for another world, but getting paid for them.
Knowing there is no goal, knowing there is no God,
I am scared that perhaps there’s no One who will be just.
Knowing the mind is poor, the willpower frail,
I am controlled by chance; life will do what it may.
But hoping stubbornly, I am still, still believing,
The work of my lifetime amounts to something.
I can welcome now the final peacefulness,
That cures all worldly pain, and our last due: death.
'''
STOP_WORDS = set('''
    the and not my no what is i
    but by that for am it 
'''.strip().split())

# data cleaning & normalisation
words = text.split()

words = (w.lower() for w in words)
words = (w for w in words if w not in STOP_WORDS)
words = (''.join(c for c in w if c.isalpha()) for w in words)

# data processing
hist = Counter(words)

# reporting
for word, count in hist.most_common(3):
    print(f'{word} appears {count} times')
    
tile_scores = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4,
               'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3,
               'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4}

def score(word):
    return sum(tile_scores.get(c, 0) for c in word)

def score_freq(word, count):
    return score(word) * count

print(f'{max(hist.items(), key=lambda kv: score_freq(*kv)) = }')
