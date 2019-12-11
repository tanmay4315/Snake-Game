import turtle
import time
import random
delay=0.1
score=0
high_score=0
wn=turtle.Screen()
wn.title("Snake Gane")
wn.bgcolor('red')
#create window
wn.setup(width=800,height=800)
wn.tracer(0)
#Snake Head
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction="stop"
#snake food
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("green")
food.penup()
food.goto(0,100)
segment=[]
#pen
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,360)
pen.write("Score:0 High Score: 0",align="center",font=("Courier",24,"normal"))
#function
def go_up():
    if head.direction!="down":
        head.direction="up"
def go_down():
    if head.direction!="up":
        head.direction="down"
def go_left():
    if head.direction!="right":
        head.direction="left"
def go_right():
    if head.direction!="left":
        head.direction="right"
def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)
# keyboard bindings
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"d")
#main game loop
while True:
    wn.update()
    # Check for collision with border
    if head.xcor() > 380 or head.xcor() < -380 or head.ycor() < -380 or head.ycor() > 340:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"
        pen.write("Snake Game")
        # Hide the segment
        for seg in segment:
            seg.goto(1200,1200)
        segment=[]
        #Reset the score
        score=0
        delay=0.1
        pen.clear()
        pen.write("Score:{} High Score:{}".format(score,high_score),align="center",font=("Courier",24,"normal"))
            
    if head.distance(food)<20:
        # Move the food to a random position
        x=random.randint(-380,380)
        y=random.randint(-360,360)
        food.goto(x,y)

        #add segement
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segment.append(new_segment)
        delay -=0.001
        # Increase the score
        initial_score=0
        score +=10
        if score-initial_score>=50:
            initial_score=score
            delay-=0.01
        if score>high_score:
            high_score=score

        pen.clear()
        pen.write("Score:{} High Score:{}".format(score,high_score),align="center",font=("Courier",24,"normal"))

    # Move the end segment first
    for index in range(len(segment)-1,0,-1):
        x=segment[index-1].xcor()
        y=segment[index-1].ycor()
        segment[index].goto(x,y)
        
    # Move segment 0 to where the head is
    if len(segment)>0:
        x=head.xcor()
        y=head.ycor()
        segment[0].goto(x,y)
    move()
    
    # Check for head collision with body
    for seg in segment:
        if seg.distance(head)<20:
            time.sleep(1)
            hewad.goto(0,0)
            head.direction="stop"
            for seg in segment:
                seg.goto(1200,1200)
            segment=[]
            score=0
            delay=0.1
            pen.clear()
            pen.write("Score:{} High Score:{}".format(score,high_score),align="center",font=("Courier",24,"normal"))
    time.sleep(delay)
wn.mainloop()
