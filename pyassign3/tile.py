#!/usr/bin/env python
# coding: utf-8

# In[ ]:




import copy
import time
import turtle

x, y, z, w, S, s, n = [0 for i in range(7)]
pieces = 0


def valid(state, i, j, a):
    global x, y, z, w, S
    if z == 1:
        list1 = []
    else:
        list1 = list(range(x - z + 2, x)) + [0]
    if w == 1:
        list2 = []
    else:
        list2 = list(range(x - w + 2, x)) + [0]
    # 判断能否横着铺
    if state == 0:
        c = i * x + j + 1
        b = c + x * (w - 1) + z - 1
        if b <= S and b - c == x * (w - 1) + z - 1 and c % x not in list1:
            for i_0 in range(i, i + w):
                for j_0 in range(j, j + z):
                    if a[i_0][j_0] == 1:
                        return False, 0
            return True, tuple([m for t in range(z - 1, -1, -1)
                                for m in range(c + z - 1 - t, b - t + 1, x)])
        return False, 0
    # 判断能否竖着铺
    if state == 1:
        c = i * x + j + 1
        b = c + x * (z - 1) + w - 1
        if b <= S and b - c == x * (z - 1) + w - 1 and c % x not in list2:
            for i_0 in range(i, i + z):
                for j_0 in range(j, j + w):
                    if a[i_0][j_0] == 1:
                        return False, 0, 0, 0
            return True, tuple([m for t in range(w - 1, -1, -1)
                                for m in range(c + w - 1 - t, b - t + 1, x)])
        return False, 0


def return_f1(a):
    """返回第一个0的坐标"""
    for (i, j) in enumerate(a):
        if 0 in j:
            return i, j.index(0)
            break


def change(a, i, j, state):
    """将已经铺过的位置换成1"""
    if state == 0:
        for i_0 in range(i, i + w):
            for j_0 in range(j, j + z):
                a[i_0][j_0] = 1
        return a
    else:
        for i_0 in range(i, i + z):
            for j_0 in range(j, j + w):
                a[i_0][j_0] = 1
        return a


def tile(a, ans, c, cnt=0):
    """递归实现铺砖过程"""
    global S, s, pieces, x, y, n
    # 如果a中的个元素均变为1，则认为已经铺完，此时将结果添加到ans中
    if a == [[1 for i in range(x)] for i in range(y)]:
        ans.append(c[:])
        n = n + 1
    else:
        i, j = return_f1(a)
        for state in 0, 1:
            if valid(state, i, j, a)[0]:
                c[cnt] = valid(state, i, j, a)[1]
                # 对a的深拷贝进行编辑
                a_copied = copy.deepcopy(a)
                a_copied = change(a_copied, i, j, state)
                tile(a_copied, ans, c, cnt + 1)


def judge_state(i, j):
    global x, y, z, w
    if j - i == x * (w - 1) + z - 1:
        return 0
    else:
        return 1


def main():
    global x, y, z, w, S, s, n, pieces
    x = int(input("Please input the length of the wall:"))
    y = int(input("Please input the width of the wall:"))
    z = int(input("Please input the length of the tile:"))
    w = int(input("Please input the width of the tile:"))
    S = x * y
    s = z * w
    n = 0
    pieces = int(S / s)
    a = [[0 for i in range(x)] for i in range(y)]
    ans = []
    c = [0 for i in range(pieces)]
    if z < w:
        z, w = w, z

    t1 = time.process_time()
    tile(a, ans, c)
    t2 = time.process_time()
    print(ans)
    print("Total: ", n)
    print("Time: ", str(t2 - t1) + "s")

    scr = turtle.Screen()
    scr.colormode(255)
    t = turtle.Turtle()
    prompt = "Input number of 0–" + str(n - 1)
    st = int(turtle.numinput("Select plan", prompt, 0, 0, n - 1))
    l = ans[st]
    length = 35
    scr.setworldcoordinates(-length * x, -length *
                            (y + x), length * 2 * x, length * x)

    t.penup()
    t.speed(0)
    t.pensize(3)
    # 给砖块勾边
    for i in l:
        if int(i[0] % x) == 0:
            t.goto(int(x - 1) * length, -int(i[0] // x - 1) * length)
        else:
            t.goto(int((i[0] % x) - 1) * length, -int(i[0] // x) * length)
        t.pendown()
        t.setheading(270)
        # 给横砖勾边
        if judge_state(i[0], i[-1]) == 1:
            for j in range(4):
                if j % 2 == 0:
                    t.forward(z * length)
                    t.left(90)
                elif j % 2 == 1:
                    t.forward(w * length)
                    t.left(90)
            t.penup()
        # 给竖砖勾边
        else:
            for j in range(4):
                if j % 2 == 0:
                    t.forward(w * length)
                    t.left(90)
                elif j % 2 == 1:
                    t.forward(z * length)
                    t.left(90)
            t.penup()

    t.hideturtle()
    scr.exitonclick()


if __name__ == "__main__":
    main()

