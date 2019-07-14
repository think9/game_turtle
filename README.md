# 거북이 공 피하기

2017년 2학기 파이썬 프로그래밍 수업 프로젝트

거북이가 움직이는 공들을 피하여 목표지점까지 도달하는 게임

Python의 turtle 라이브러리를 이용하여 구현

개발 Issue

<h3>#1. 최초 시작 시 공(장애물)의 생성 및 이동</h3>

공의 최초 위치는 랜덤하게 생성

공의 진행방향을 결정하기 위하여 랜덤하게 dx, dy의 값을 설정하여 주는데 이 때, 두 값이 모두 0으로 설정되지 않도록 방지

공이 화면 밖을 벗어나는 것을 방지하기 위하여 공이 벽과 만났을 시 dx, dy 값에 -1 값을 곱해줌으로써 이동방향을 반대로 변경

공의 색상 또한 랜덤하게 결정

```python
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
```

<h3>#2. 거북이와 공의 충돌 구현</h3>

거북이는 키보드 이벤트를 통하여 이동

거북이와 공의 충돌을 체크하기 위하여 거북이의 위치와 공 사이의 거리를 계산하는 함수를 구현

```python
def distance(x1, y1, x2, y2):
  return ((x2-x1)**2+(y2-y1)**2)**0.5
```

거북이와 공 중심 사이의 거리가 임계치보다 작다면 충돌로 판정

충돌로 판정 시 진행방향(dx, dy)에 -1을 곱하여 반대 방향으로 이동하도록 함

```python
#if crush occured
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
```
