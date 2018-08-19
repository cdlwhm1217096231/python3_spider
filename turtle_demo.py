#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-02 19:55:25
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$

import turtle as t
import time
"""
1、画布
设置画布大小: turtle.screensize(canvwidth=, canvheight=, bg=None)
turtle.screensize(800, 600, "green")
turtle.screensize()  # 默认返回大小为400*300的画布

turtle.setup(width=0.5, height=0.75, startx=None, starty=None)
width, height: 输入宽和高为整数时, 表示像素; 为小数时, 表示占据电脑屏幕的比例
(startx, starty): 表示矩形窗口左上角顶点的位置;如果为空,则窗口位于屏幕中心

2、画笔

2.1 画笔的状态
在画布上,默认有一个坐标原点为画布中心的坐标轴, 坐标原点上有一只面朝x轴正方向小乌龟. 
这里我们描述小乌龟时使用了两个词语:坐标原点(位置),面朝x轴正方向(方向),就是使用位置方向描述小乌龟(画笔)的状态

2.2 画笔的属性
turtle.pensize()：设置画笔的宽度
turtle.pencolor(): 没有参数传入,返回当前画笔颜色；传入参数设置画笔颜色,可以是字符串如"green"、"red",也可以是RGB 3元组
				pencolor('brown')
				tup = (0.2, 0.8, 0.55)
				pencolor(tup)
turtle.speed(speed): 设置画笔移动速度,画笔绘制的速度范围[0,10]整数, 数字越大越快
 2.3 绘图命令
 操纵海龟绘图有着许多的命令,这些命令可以划分为3种:一种为运动命令，一种为画笔控制命令,一种是全局控制命令

 2.3.1 画笔运动命令

 turtle.forward(distance)	向当前画笔方向移动distance像素长
 turtle.backward(distance)	向当前画笔相反方向移动distance像素长度
 turtle.right(degree)	顺时针移动degree°
 turtle.left(degree)	逆时针移动degree°
 turtle.pendown()	移动时绘制图形,缺省时也为绘制
 turtle.goto(x,y)	将画笔移动到坐标为x,y的位置
 turtle.penup()	移动时不绘制图形,提起笔，用于另起一个地方绘制时用
 turtle.speed(speed)	画笔绘制的速度范围[0,10]整数
 turtle.circle()	画圆,半径为正(负),表示圆心在画笔的左边(右边)画圆

 2.3.2 画笔控制命令

turtle.pensize(width)	绘制图形时的宽度
turtle.pencolor()	画笔颜色
turtle.fillcolor(colorstring)	绘制图形的填充颜色
turtle.color(color1, color2)	同时设置pencolor=color1, fillcolor=color2
turtle.filling()	返回当前是否在填充状态
turtle.begin_fill()	准备开始填充图形
turtle.end_fill()	填充完成；
turtle.hideturtle()	隐藏箭头显示；
turtle.showturtle()	与hideturtle()函数对应

2.3.3 全局控制命令

turtle.clear()	清空turtle窗口，但是turtle的位置和状态不会改变
turtle.reset()	清空窗口，重置turtle状态为起始状态
turtle.undo()	撤销上一个turtle动作
turtle.isvisible()	返回当前turtle是否可见
stamp()	复制当前图形
turtle.write(s[,font=("font-name",font_size,"font_type")])	写文本，s为文本内容，font是字体的参数，里面分别为字体名称，大小和类型；font为可选项, font的参数也是可选项

3.命令详解

3.1 turtle.circle(radius, extent=None, steps=None)
描述: 以给定半径画圆
参数:
radius(半径); 半径为正(负),表示圆心在画笔的左边(右边)画圆
extent(弧度) (optional);
steps (optional) (做半径为radius的圆的内切正多边形,多边形边数为steps)

举例:
circle(50) # 整圆;
circle(50,steps=3) # 三角形;
circle(120, 180) # 半圆
"""
# 太阳花实例
# t.color("yellow", "blue")
# t.speed(10)
# t.begin_fill()
# for _ in range(50):
#     t.forward(200)
#     t.left(170)
# t.end_fill()
# time.sleep(1)
# 画出正方形程序
# t.color('red', 'green')
# t.speed(3)
# t.begin_fill()
# for _ in range(4):
#     t.forward(100)
#     t.right(90)
# t.left(-90)
# t.circle(50, -180)
# t.end_fill()
# time.sleep(10)

# 绘制小蟒蛇


def Snake(rad, angle, len, neckrad):
    for _ in range(len):
        t.circle(rad, angle)
        t.circle(-rad, angle)
    t.circle(rad, angle / 2)
    t.forward(rad / 2)  # 直线前进
    t.circle(neckrad, 180)
    t.forward(rad / 4)
    time.sleep(5)


if __name__ == "__main__":
    t.setup(1500, 1400, 0, 0)
    t.pensize(30)  # 画笔尺寸
    t.pencolor("green")
    t.seth(-40)    # 前进的方向
    Snake(70, 80, 2, 15)
