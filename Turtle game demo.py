''' for i in range(20):
        if player_one.pos() >= (300,100):
             print("Player One Wins!")
             break
        elif player_two.pos() >= (300,-100):
             print("Player Two Wins!")
             break
        else:
             player_one_turn = input("Press 'Enter' to roll the die ")
             die_outcome = random.choice(die)
             print("The result of the die roll is: ")
             print(die_outcome)
             print("The number of steps will be: ")
             print(20*die_outcome)
             player_one.fd(20*die_outcome)
             player_two_turn = input("Press 'Enter' to roll the die ")
             d = random.choice(die)
             print("The result of the die roll is: ")
             print(die_outcome)
             print("The number of steps will be: ")
             print(20*die_outcome)
             player_two.fd(20*die_outcome)'''

import turtle

t = turtle.Turtle()

#making a square using for loop
'''t.speed(1)
for i in range (0,4):
    t.fd(100)
    t.rt(90)'''

#practise 
'''t.goto(100,200)
t.home()
t.circle(60)
t.dot(120)'''

turtle.title("My turtle program")
#turtle.bgpic("naturebridge1.gif")
'''turtle.bgcolor("red")
t.color("yellow","blue")

#color = input("enter the color: ")
t.fillcolor("blue")
t.begin_fill()
for i in range (0,4):
    t.fd(100)
    t.rt(90)
t.end_fill()
t.lt(90)
t.fd(100)
t.fillcolor("blue")
t.begin_fill()
t.circle(100,180)
t.lt(90)
t.fd(200)
t.end_fill()
t.home()
t.up()
t.goto(-100,-100)
t.down()
t.circle(60,steps=6)
t.lt(90)
t.fd(60)'''

'''
turtle.bgcolor("lightblue")
t.pensize(5)
t.lt(90)
t.up()
t.bk(180)
t.lt(90)
t.fd(100)
t.rt(90)
t.down()
t.fd(350)
t.rt(90)
t.fd(200)
t.rt(90)
t.fd(150)
t.rt(90)
t.fd(200)
t.rt(90)
t.fd(50)
t.rt(90)
t.pensize(1)
t.fd(200)
t.lt(90)
t.fd(50)
t.lt(90)
t.fd(200)
t.bk(75)
t.lt(90)
t.up()
t.fd(25)
t.down()
t.circle(25)
t.lt(90)
t.fd(25)
t.speed(2)
for i in range (0,24):
    t.lt(15)
    t.fd(25)
    t.bk(25)'''

list1 = ["purple", "red", "blue", "green", "orange"]
for i in range(200):
    t.color(list1[i%5])
    t.pensize(i/10+1)
    t.forward(i)
    t.lt(59)


    
turtle.done()
