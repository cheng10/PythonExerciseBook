import string
import operator

count = {}
with open('input.txt') as f:
    for line in f:
        line = line.translate(None, string.punctuation)
        line = line.lower()
        for word in line.split():
            if word not in count:
                count[word] = 1
            else:
                count[word] += 1

sorted_count = sorted(count.items(), key=operator.itemgetter(1), reverse=True)
for item in sorted_count:
    print(item)
