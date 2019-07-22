from collections import Counter
import operator
n = int(input())
while n >0:
    counts=dict(Counter(input().lower()))
    ocorrencias = ''
    counts = {key: value for key, value in counts.items() if key.isalpha()}
    for key, value in counts.items():
        if value==counts[max(counts.items(), key=operator.itemgetter(1))[0]]:
            ocorrencias = ocorrencias+key
    print(''.join(sorted(ocorrencias)))
    n=n-1