# coding=utf-8
"""
Function:
    质点匀速圆周运动
Author:
    陈宇铭
"""
from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animmation

# 参数
# π
Pi = np.pi
# 坐标轴参数
x_limit = [-5, 5]
y_limit = [-5, 5]
z_limit = [-5, 5]
x0, y0, z0 = 0, 0, 0
r0 = 5  # 中心点半径


# 绘制点
class Point():
    def __init__(self):
        # 运动参数
        self.V = 10  # 速度
        self.R = 5  # 圆周半径
        self.r = 10  # 物体半径
        self.W = 2 * Pi  # 角速度
        self.t_range = np.arange(0, 1 + 0.005, 0.005)  # 周期
        # 初始化
        t = 0
        x = x0 + self.R * np.cos(self.W * t)
        y = y0 + self.R * np.sin(self.W * t)
        z = z0
        self.point, = ax.plot([x], [y], [z], marker='o', color='black', markersize=self.r)
        self.data = [[x0 + self.R * np.cos(self.W * self.t_range[i]), y0 + self.R * np.sin(self.W * self.t_range[i]), z0] for i in
                     range(1, len(self.t_range))]

    def gen(self):
        # 绘制轨迹
        x = x0 + self.R * np.cos(self.W * self.t_range)
        y = y0 + self.R * np.sin(self.W * self.t_range)
        z = z0
        track = ax.plot(x, y, z, color='blue')
        return track,

    def update(self, data):
        self.point.set_data([data[0], data[1]])
        self.point.set_3d_properties(data[2])
        return self.point,

    def run(self):
        T = self.V / self.R
        ani = animmation.FuncAnimation(fig, self.update, frames=self.data, init_func=self.gen, interval=T)
        plt.show()

# 绘制画板
def draw_plot(w,h):
    fig = plt.figure(figsize=(w,h))
    plt.subplot(111)
    ax = Axes3D(fig)
    ax.set_xlim(x_limit)
    ax.set_ylim(y_limit)
    ax.set_zlim(z_limit)
    ax.plot([x0], [y0], [z0], marker='o', color='red', markersize=r0)
    return fig, ax


if __name__ == "__main__":
    fig, ax = draw_plot(8,8)
    point = Point()
    point.run()

