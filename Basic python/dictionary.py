person = {"name": "labib", "age": 22, "job": "student"}
print(person)
for i in person:
    print(i)

for i in person:
    print(person[i])

person["uni"] = "kiu"
print(person)
print(person.keys())
print(person.values())

for k, v in person.items():
    print(k, v)
