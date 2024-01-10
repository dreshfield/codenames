#!/usr/bin/env python3

import itertools, random
import argparse as ap
import pathlib as p

parser = ap.ArgumentParser(description='Generates random codenames in the style of U.S. military/intelligence operations')
parser.add_argument('-a', '--alpha', dest='alpha', action='store_true', help='display results in alphabetical, rather than random, order')
parser.add_argument('-n', '--number', type=int, dest='n', action='store', help='specify number of results to return (default: 20)')
args = parser.parse_args()

script_dir = p.Path(__file__).resolve(strict=True).parent

def load_words(filename):
    with open(filename) as f:
        words = [line.split() for line in f]
    return ([word for word, count in words],
            list(itertools.accumulate(int(count) for word, count in words)))

adjs, adjs_weights = load_words(p.Path.joinpath(script_dir, 'words/adj.txt'))
nouns, nouns_weights = load_words(p.Path.joinpath(script_dir, 'words/noun.txt'))
names_list = []

if not args.n:
    n = 20
else:
    n = args.n

# TODO: This works, but can probably be done more cleanly
for _ in range(n):
    while True:
        adj = random.choices(adjs, cum_weights=adjs_weights)[0]
        noun = random.choices(nouns, cum_weights=nouns_weights)[0]
        if len(adj) >= 3 and len(noun) >= 3:
            break
    if args.alpha:
        names_list.append(' '.join((str.upper(adj), str.upper(noun))))
    else:
        print(str.upper(adj), str.upper(noun))

if args.alpha:
    names_list.sort()
    print(*names_list, sep='\n')