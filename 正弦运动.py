"""
Function:
    质点按照正弦曲线移动
Author:
    陈宇铭
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# 坐标轴参数
A = 2
x_limit = [0, 2 * np.pi]


# 绘制点
class Point:
    def __init__(self):
        # 周期
        self.T = 10
        # 物体半径
        self.R = 10
        self.data = [[i, np.sin(i)] for i in np.linspace(*x_limit, 200)]
        self.point, = ax.plot([], [], marker='o', color='black', markersize=self.R)

    def gen(self):
        return line

    def update(self, data):
        self.point.set_data(data[0], data[1])
        return self.point,

    def run(self):
        ani = animation.FuncAnimation(fig, self.update, frames=self.data, interval=self.T, init_func=self.gen)
        plt.show()


# 绘制画板
def draw_plot():
    fig, ax = plt.subplots()
    ax.set_xlim(x_limit)
    ax.set_ylim(-A, A)
    x = np.linspace(*x_limit)
    y = np.sin(x)
    line = ax.plot(x, y)
    return fig, ax, line


if __name__ == "__main__":
    fig, ax, line = draw_plot()
    point = Point()
    point.run()
