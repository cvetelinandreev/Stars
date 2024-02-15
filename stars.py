from turtle import *


def star(size, k, n):
    for i in range(n):
        forward(size)
        right(k * 360 / n)


star(100, 2, 5)

input()
