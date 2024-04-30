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
    pass


def graph_1(master, a, b, c):
    pass


def graph_2(master, a, b, c, choose):
    pass


def graph_3(master, a1, a2, b1, b2, c1, c2):
    pass
