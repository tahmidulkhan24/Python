import turtle

name = turtle.textinput("Name", "What is your name?")

if name is None:
    print("No input provided")
    turtle.exitonclick()
    exit()

name = name.lower()

if name.startswith("mr"):
    print("Hello Sir")
elif name.startswith("miss") or name.startswith("mrs"):
    print("Hello Ma'am")
else:
    name = name.capitalize()
    message = f"Hi {name}, how are you?"
    print(message)

turtle.exitonclick()