a, b = map(int, input().split())
flg = False
for i in range(a, b + 1):
    s = str(i)
    if all(c in "47" for c in s):
        print(i, end=" ")
        flg = True
if flg == False:
    print("-1")
