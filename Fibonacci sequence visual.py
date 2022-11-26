import turtle

print("Welcome to the Fibonacci Visualizer 2.0!")
extent = int(input("Enter the number of fibonacci sequence to visualize: "))

r = [0, 1]

for i in range(extent):
    r.append(r[0+i] + r[1+i])

#remove comment for printing the sequence
#for i in range(extent):
#    print(r[i])

fibo = turtle.Turtle()
fibo.color("white")
fibo.penup()
#fibo.goto(0, -250)
fibo.pendown()

#scalers
if extent <= 15:
    for i in range(extent):
        r[i] = r[i]
elif extent < 20:
    for i in range(extent):
        r[i] = r[i] / 10
elif extent < 30:
    for i in range(extent):
        r[i] = r[i] / 20
elif extent < 40:
    for i in range(extent):
        r[i] = r[i] / 30
elif extent >= 50:
    for i in range(extent):
        r[i] = r[i] / 100

ws = turtle.Screen()
ws.bgcolor("darkgreen")

for i in range(extent):
    fibo.circle(r[i], 90)

ws.exitonclick()