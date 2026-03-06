res=0
for num in range(40):
    res=res+num
print(res)

a=[0,22,1,3,12,41,21,4,312,321]
max_num=a[0]
for n in a:
    if n>max_num:
        max_num=n

print(max_num)