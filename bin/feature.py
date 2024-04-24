from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np


# Vị trí xuất hiện cửa sổ
def center_window(win):
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    win_width = win.winfo_width()
    win_height = win.winfo_height()
    x = (screen_width // 2) - (win_width // 2)
    y = (screen_height // 2) - (win_height // 2) - 120
    win.geometry(f"+{x}+{y}")


# Hàm quản lí thông báo lỗi
def alert_box(code):
    if code == 1:
        messagebox.showerror(title="ZeroDivisionError", message="a ≠ 0")
    elif code == 2:
        messagebox.showerror(title="ValueError", message="Hệ số không được để trống")
    elif code == 3:
        messagebox.showerror(title="UnboundLocalError", message="Chưa chọn dấu")


# Hàm vẽ đồ thị
def draw(master, plot, width, height, x, y):
    canvas = FigureCanvasTkAgg(plot, master=master)
    canvas.get_tk_widget().config(width=width, height=height)
    canvas.draw()
    canvas.get_tk_widget().place(x=x, y=y)  # Hiển thị GUI


def graph_1(master, a, b, c):
    x_values = np.linspace(-10, 10, 100)
    # Tính giá trị y tương ứng với mỗi x
    y_values = a * x_values**2 + b * x_values + c
    # Vẽ đồ thị
    fig, ax = plt.subplots()
    plt.plot(x_values, y_values, label=f"{a}x^2 + {b}x + {c} = 0")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axhline(0, color="gray", linestyle="--")  # Đường ngang y=0
    plt.axvline(0, color="gray", linestyle="--")  # Đường dọc x=0
    plt.grid(True)
    plt.legend(fontsize=6)
    draw(master, fig, 308, 230, 20, 180)
    plt.close(fig)


def graph_2(master, a, b, c, choose):
    x_values = np.arange(-5, 5, 0.1)
    # Tính giá trị y tương ứng với mỗi x
    y_values = a * x_values**2 + b * x_values + c
    # Vẽ đồ thị
    fig, ax = plt.subplots()
    if choose == ">" or choose == "≥":
        if choose == ">":
            plt.plot(x_values, y_values, label=f"{a}x^2 + {b}x + {c} > 0", color="blue")
        elif choose == "≥":
            plt.plot(
                x_values, y_values, label=f"{a}x^2 + {b}x + {c} >= 0", color="blue"
            )
        plt.fill_between(
            x_values, 0, y_values, where=(y_values > 0), color="gray", alpha=0.3
        )
    if choose == "<" or choose == "≤":
        if choose == "<":
            plt.plot(x_values, y_values, label=f"{a}x^2 + {b}x + {c} < 0", color="blue")
        elif choose == "≤":
            plt.plot(
                x_values, y_values, label=f"{a}x^2 + {b}x + {c} <= 0", color="blue"
            )
        plt.fill_between(
            x_values, 0, y_values, where=(y_values < 0), color="gray", alpha=0.3
        )
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axhline(0, color="gray", linestyle="--")  # Đường ngang y=0
    plt.axvline(0, color="gray", linestyle="--")  # Đường dọc x=0
    plt.grid(True)
    plt.legend(fontsize=6)
    draw(master, fig, 308, 230, 20, 180)
    plt.close(fig)


def graph_3(master, a1, a2, b1, b2, c1, c2):
    x_values = np.linspace(-10, 10, 100)
    y_values1 = (c1 - a1 * x_values) / b1
    y_values2 = (c2 - a2 * x_values) / b2
    # Vẽ đồ thị
    fig, ax = plt.subplots()
    plt.plot(x_values, y_values1, label=f"{a1}x - {abs(b1)}y = {c1}")
    plt.plot(x_values, y_values2, label=f"{a2}x + {b2}y = {c2}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axhline(0, color="gray", linestyle="--")  # Đường ngang y=0
    plt.axvline(0, color="gray", linestyle="--")  # Đường dọc x=0
    plt.grid(True)
    plt.legend(fontsize=6)
    draw(master, fig, 308, 230, 20, 260)
    plt.close(fig)
