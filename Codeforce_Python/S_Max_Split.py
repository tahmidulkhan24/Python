s = input()
cntl = 0
cntr = 0
res = []
st = 0
for i, ch in enumerate(s):
    if ch == "L":
        cntl += 1
    else:
        cntr += 1
    if cntl == cntr:
        res.append(s[st : i + 1])
        st = i + 1
        cntl = 0
        cntr = 0

print(len(res))

for part in res:
    print(part)
