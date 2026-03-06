num = [10, 20, 30, 40, 40, 40, 70, 80]

print(num[2:5])
print(num[2:5:2])
print(num[:])
print(num[5:1:-2])
print(num[::-1])
num.append(100)
print(num)
num2 = num.copy()
print(num2)
cnt = num.count(40)
print(cnt)
num.extend(num2)
print(num)
num.insert(5, 121)
num.pop(6)
print(num)
num.remove(100)
print(num)
num.sort()
print(num)
num.sort(reverse=True)
newlist = sorted(num, reverse=True)
print(newlist)

arr = [22, 42, 12, 10, 33, 1233, 12, 44, 67, 12, 57, 213, 33]
odd_num = [i for i in arr if i % 2 == 1]  # list comprehension
print(odd_num)
name = ["labib", "ovi", "badhan", "shoab"]
age = [22, 23, 24, 10]
comb1 = []
for n in name:
    for ag in age:
        comb1.append({n, ag})  # give me all possible combination

print(comb1)  # print the combination

comb2 = [(n, a) for n in name for a in age]  # list comprehension
