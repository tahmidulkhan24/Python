from collections import Counter

n = int(input())
a = list(map(int, input().split()))
rem = 0
freq = Counter(a)
for c, cnt in freq.items():
    if c == cnt:
        continue
    elif cnt > c:
        rem = rem + cnt - c
    else:
        rem = rem + cnt

print(rem)
