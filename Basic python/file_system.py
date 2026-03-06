with open("massage.txt", "w") as file:
    file.write("wow,i know file")
with open("massage.txt", "a") as file:
    file.write("wow,i know file")

with open("massage.txt", "r") as file:
    text = file.read()
    print(text)
