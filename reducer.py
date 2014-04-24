#!/usr/bin/env python

import operator 
import sys

freq = {}
top_words=[]
i = 0

for line in sys.stdin:
    # removes all whitespaces
    line = line.strip()
    word, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        continue
    freq[word]= freq.get(word, 0) + 1

sorted_words = sorted(freq.iteritems(), key=operator.itemgetter(1), reverse=True)

for pair in sorted_words:
	print pair
	i = i + 1
	if i == 100:
		break
