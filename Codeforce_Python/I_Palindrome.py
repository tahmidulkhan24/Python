n = input()
rev = n[::-1]
new_rep = int(rev)
print(new_rep)
if n == rev:
    print("YES")
else:
    print("NO")
