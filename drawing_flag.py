import turtle
import math

turtle.pensize(3)
turtle.colormode(255)

# 画背景
turtle.pencolor("#ed120c")
turtle.fillcolor("#ed120c")
turtle.begin_fill()
turtle.penup()
turtle.goto(-150, 100)
turtle.pendown()

for i in [300, 200, 300, 200]:
    turtle.forward(i)
    turtle.right(90)
turtle.left(90)
turtle.end_fill()
turtle.penup()


# 画五角星函数，要求传入五角星中心坐标，五角星外接圆半径，五角星逆时针旋转角度（默认角度0度为向上，即大五角星方向）
def Pentagram(x, y, radius, degree):
    length = (radius * math.sqrt(8) // 3) * 2  # 根据五角星外接圆半径计算五角星长度

    turtle.goto(x, y)  # 五角星外接圆中心坐标（即五角星中心坐标）
    turtle.left(degree)  # 五角星逆时针旋转多少度
    turtle.forward(radius)  # 前进外接圆半径距离，到达五角星顶点
    turtle.pendown()

    # 以下为标准画五角星代码，画笔颜色及填充颜色可以通过取色器取
    turtle.right(162)
    turtle.pencolor("#f4ec20")
    turtle.fillcolor("#f4ec20")
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(length)
        turtle.right(144)
    turtle.end_fill()
    turtle.left(162)

    turtle.right(degree)
    turtle.penup()


# 画大五角星
Pentagram(-100, 50, 30, 0)

# 画第一个小五角星
degree1 = 90 + math.atan(3 / 5) * 180 / math.pi  # 计算第一个小五角星相对于大五角星的逆时针旋转角度，atan计算弧度需要转化为角度
Pentagram(-50, 80, 10, degree1)

# 画第二个小五角星
degree2 = 90 + math.atan(1 / 7) * 180 / math.pi
Pentagram(-30, 60, 10, degree2)

# 画第三个小五角星
degree3 = 90 - math.atan(2 / 7) * 180 / math.pi
Pentagram(-30, 30, 10, degree3)

# 画第四个小五角星
degree4 = 90 - math.atan(4 / 5) * 180 / math.pi
Pentagram(-50, 10, 10, degree4)
turtle.goto(100, -10)
turtle.write("爱你中国")

turtle.hideturtle()
turtle.done()