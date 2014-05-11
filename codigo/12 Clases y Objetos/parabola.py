from visual import *

floor = box(length=4, height=0.5, width=24, color=color.blue)

ball = sphere(pos=(0,0,0), color=color.red)

Vx = 1
Vy = 1
ball.velocity = vector(Vx,Vy,0)

dt = 0.01

while 1:
    rate(100)
    #ball.pos = ball.pos + ball.velocity*dt

    ball.pos.x += Vx*dt

    ball.pos.y += Vy*dt - 0.5*9.8*(dt ** 2)
    
    
    #if ball.y >  5:
    #    ball.velocity.y = -ball.velocity.y
    #else:
    #    ball.velocity.y = ball.velocity.y - 9.8*dt
