import turtle as t
t.shape('turtle')
t.pen(speed=20,pensize=5)
#=========================== Mouth ===========================
def draw_mouth(rad1,rad2,rad3):
 for i in range(1):
     t.seth(90)
     t.circle(rad1,90)
     t.circle(rad1,90)
     t.circle(rad2,90)
     t.circle(rad2,90)
     t.penup()
     t.home()
     t.seth(270)
     t.pendown()
     for i in range(1):
        t.circle(rad3,45)
        t.circle(rad3,60)
     t.penup()
     t.goto(-100,100)

#=========================== Head ===========================
def draw_body(length,rad1):
    t.seth(90)
    t.pendown()
    t.circle(rad1,240)
    t.penup()
    t.seth(-80)
    t.pendown()
    t.fd(length)
    t.penup()
    t.fd(-1*length)
    t.rt(-80)
    t.bk(128)
    t.rt(100)
    t.pendown()
    t.fd(100)
    t.penup()
#=========================== Eyes ===========================
def draw_eyes(rad1,rad2):
    t.goto (10,170)
    t.pendown()
    t.seth(90)
    for i in range(2):
        t.circle(rad1,90)
    t.fd(30)
    for j in range(2):
        t.circle(rad1,90)
    t.fd(30)
    t.penup()
    t.goto (90,170)
    t.pendown()
    for k in range(2):
        t.circle(rad2,90)
    t.fd(30)
    for l in range(2):
        t.circle(rad2,90)
    t.fd(30)
    t.penup()

#=========================== Start =========================== 
draw_mouth(100,75,-75)
draw_body(100,-150)
draw_eyes(10,10)
t.hideturtle()
#===========================  END  ===========================



