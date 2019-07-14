from turtle import *
import random

#키보드 이벤트
#왼쪽 이동
def key_left():
    my.seth(180)
    my.fd(step)
    if(my.xcor()<-300):
        my.setx(-300)

#오른쪽 이동
def key_right():
    my.seth(0)
    my.fd(step)
    if(my.xcor()>300):
        my.setx(300)

#위쪽 이동
def key_up():
    my.seth(90)
    my.fd(step)
    if(my.ycor()>300):
        my.sety(300)

#아래쪽 이동
def key_down():
    my.seth(270)
    my.fd(step)
    if(my.ycor()<-300):
        my.sety(-300)


#최초 공(장애물) 생성
#좌표(x, y)와 이동 방향(dx, dy) 및 색상을 랜덤하게 생성 후 반환
def make_ball(size):
    x = random.randint(-200, max_x)
    y = random.randint(min_y, 200)
    color = random.choice(["red", "green", "blue", "yellow", "pink", "purple"])
    while True:
        dx = random.randint(-1, 1)  # 이동벡터
        dy = random.randint(-1, 1)  # 이동벡터
        if dx != 0 or dy != 0:
            break
    return [x, y, size, color, dx, dy]

#거리계산 함수, 피터고라스의 정리 이용
def distance(x1, y1, x2, y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5

#움직이는 공
def animate_ball(pen, ball_list):
    tracer(False)
    game=True
    death=0
    while game:
        listen()
        pen.clear()  # 공을 지움
        #공의 이동
        for i in range( len(ball_list) ):
            ball_x, ball_y, size, color, dx, dy =  ball_list[i]
            ball_x += dx
            ball_y += dy
            ball_list[i][0] = ball_x
            ball_list[i][1] = ball_y
            #거북이와 공의 충돌 -> 데스 카운트 +1
            if(distance(my.xcor(), my.ycor(), ball_x, ball_y)<=15):
                my.setpos(-goal, goal)
                death = death+1
            #공의 좌표가 화면을 벗어날 시 이동 벡터에 -1 값을 곱하여 반대방향으로 움직이도록 함
            if (ball_x<min_x) or (ball_x > max_x): ball_list[i][4] *= -1
            if (ball_y<min_y) or (ball_y > max_y): ball_list[i][5] *= -1
            #공과 공의 충돌 판정
            #중심 좌표 간 거리를 이용하여 충돌 판정을 구현
            for j in range(len(ball_list)) :
                if(not i==j):
                    ball2_x=ball_list[j][0]
                    ball2_y=ball_list[j][1]
                    if(distance(ball_x, ball_y, ball2_x, ball2_y)<=ball_size):
                        ball_list[i][4] *= -1
                        ball_list[i][5] *= -1
                        ball_list[j][4] *= -1
                        ball_list[j][5] *= -1
                        ball_list[i][0] += ball_list[i][4]*2
                        ball_list[i][1] += ball_list[i][5]*2
                        ball_list[j][0] += ball_list[j][4]*2
                        ball_list[j][1] += ball_list[j][5]*2
            pen.setpos(ball_x, ball_y)
            pen.dot(size, color)
        #목표지점 도착
        if(goal<=my.xcor()<=goal+20 and -goal-20<=my.ycor()<=-goal):
                game=False
                return death
        update() # 스크린 갱신
            

def main():
    global min_x, max_x, min_y, max_y, ball_size, goal, step
    #기본 설정 (창의 크기, 볼의 크기, 목표 위치, 이동 거리)
    max_x = 300; min_x=  -max_x
    max_y = 300; min_y = -max_y
    ball_size=20
    goal=250
    step=20
    setup(max_x*2, max_y*2)

    global my
    my=Turtle()
    my.up()
    #도착지점을 그림
    my.setpos(goal, -goal)
    my.down()
    my.seth(0)
    my.fd(20)
    my.seth(270)
    my.fd(20)
    my.seth(180)
    my.fd(20)
    my.seth(90)
    my.fd(20)
    my.up()

    #기본 설정
    my.shape("turtle")
    my.setpos(-goal,goal)
    #my.down()
    onkey(key_right, "Right")
    onkey(key_left, "Left")
    onkey(key_up, "Up")
    onkey(key_down, "Down")

    my_pen = Turtle()
    my_pen.up()
    my_pen.ht()
    ball_list = []
    #공 생성 정보를 받아와 리스트에 추가
    for i in range(20):
        ball = make_ball(ball_size)
        ball_list.append(ball)
    deathCount=animate_ball(my_pen, ball_list) # 에니메이션
    print("Goal in! Death Count : %d"%(deathCount))
    
#설명4   
if __name__ == "__main__":
    main()
