import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import numpy as np
import math


# Vị trí xuất hiện cửa sổ
def center_window(win):
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    win_width = win.winfo_width()
    win_height = win.winfo_height()
    x = (screen_width // 2) - (win_width // 2)
    y = (screen_height // 2) - (win_height // 2) - 120
    win.geometry(f"+{x}+{y}")


win = tk.Tk()
win.title("X math")
win.geometry("350x160")
win.resizable(width=False, height=False)
win.attributes("-topmost", True)
win.iconbitmap("image/icon/Calculator_30001.ico")
center_window(win)


# Hàm quản lí thông báo lỗi
def alert_box(code):
    if code == 1:
        messagebox.showerror(title="ZeroDivisionError", message="a ≠ 0")
    elif code == 2:
        messagebox.showerror(title="ValueError", message="Hệ số không được để trống")
    elif code == 3:
        messagebox.showerror(title="UnboundLocalError", message="Chưa chọn dấu")


# Chương trình con giải phương trình bậc 2
def click_pt_bt():
    win1 = tk.Tk()
    win1.title("Giải phương trình bậc 2")
    win1["bg"] = "#344953"
    win1.geometry("350x440")
    win1.resizable(width=False, height=False)
    win1.iconbitmap("image/icon/Calculator_30001.ico")

    khung_1 = tk.Label(win1, width=43, height=5, bg="#ffffff")
    khung_1.place(x=20, y=10)

    def load_khung_2():
        khung_2 = tk.Label(win1, width=43, height=4, bg="#ffffff")
        khung_2.place(x=20, y=103)

    # Hàm tính toán
    def solve_1():

        load_khung_2()
        try:
            a = float(a_in.get())
            b = float(b_in.get())
            c = float(c_in.get())
        except:
            alert_box(2)

        if a == 0:
            alert_box(1)

        denta = pow(b, 2) - (4 * a * c)
        denta_out = tk.Label(
            win1, text="  Δ = " + str(denta), font=("Arial", 12), bg="#ffffff"
        )
        denta_out.place(x=20, y=105)

        if denta > 0:
            can_denta = float(math.sqrt(denta))
            x1 = float((-b + can_denta) / (2 * a))
            x2 = float((-b - can_denta) / (2 * a))
            x1_out = tk.Label(
                win1, text="  x1 = " + str(x1), font=("Arial", 12), bg="#ffffff"
            )
            x1_out.place(x=20, y=125)

            x2_out = tk.Label(
                win1, text="  x2 = " + str(x2), font=("Arial", 12), bg="#ffffff"
            )
            x2_out.place(x=20, y=145)

        elif denta == 0:
            x = x1 = x2 = -b / (2 * a)
            x_out = tk.Label(
                win1, text="  x = " + str(x), font=("Arial", 12), bg="#ffffff"
            )
            x_out.place(x=20, y=125)

        else:
            rong_out = tk.Label(
                win1,
                text="Vô nghiệm",
                font=("Arial", 12),
                bg="#ffffff",
            )
            rong_out.place(x=20, y=145)

        # Vẽ đồ thị phương trình bậc 2
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

        canvas = FigureCanvasTkAgg(fig, master=win1)
        canvas.get_tk_widget().config(width=308, height=230)
        canvas.draw()

        # Hiển thị GUI
        canvas.get_tk_widget().place(x=20, y=180)

        plt.close(fig)

    # Thiết kế giao diện
    text_1 = tk.Label(win1, text=("Nhập hệ số:"), font=("Arial", 12), bg="#ffffff")
    text_1.place(x=20, y=10)

    text_2 = tk.Label(
        win1, text=("ax² + bx + c = 0  (a ≠ 0)"), font=("Arial", 12), bg="#ffffff"
    )
    text_2.place(x=60, y=35)

    text_input = tk.Label(
        win1,
        text=("a:                       b:                       c:"),
        font=("Arial", 12),
        bg="#ffffff",
    )
    text_input.place(x=20, y=65)

    a_in = tk.Entry(win1, font=("Arial", 12), bg="#f0f0f0", width=8, justify="left")
    a_in.focus()
    a_in.place(x=38, y=69)

    b_in = tk.Entry(win1, font=("Arial", 12), bg="#f0f0f0", width=8, justify="left")
    b_in.place(x=145, y=69)

    c_in = tk.Entry(win1, font=("Arial", 12), bg="#f0f0f0", width=8, justify="left")
    c_in.place(x=250, y=69)

    check_bt = tk.Button(
        win1, text="Giải", font=("Arial", 12), width=6, height=1, command=solve_1
    )
    check_bt.place(x=262, y=28)

    load_khung_2()

    khung_3 = tk.Label(win1, width=43, height=15, bg="#ffffff")
    khung_3.place(x=20, y=180)


# Chương trình con giải bất phương trình bậc 2
def click_bpt_bt():
    win2 = tk.Tk()
    win2.title("Giải bất phương trình bậc 2")
    win2["bg"] = "#344953"
    win2.geometry("350x440")
    win2.resizable(width=False, height=False)
    win2.iconbitmap("image/icon/Calculator_30001.ico")

    khung_1 = tk.Label(win2, width=43, height=5, bg="#ffffff")
    khung_1.place(x=20, y=10)

    def load_khung_2():
        khung_2 = tk.Label(win2, width=43, height=4, bg="#ffffff")
        khung_2.place(x=20, y=103)

    # Hàm tính toán
    def solve_2():

        load_khung_2()
        try:
            a = float(a_in.get())
            b = float(b_in.get())
            c = float(c_in.get())
        except:
            alert_box(2)

        choose = str(choose_in.get())

        if a == 0:
            alert_box(1)

        denta = pow(b, 2) - (4 * a * c)
        denta_out = tk.Label(
            win2, text=" Δ = " + str(denta), font=("Arial", 12), bg="#ffffff"
        )
        denta_out.place(x=20, y=105)

        try:
            if denta < 0:
                if choose == ">":
                    if a > 0:
                        khoang = tk.Label(
                            win2,
                            text=("Tất cả số thực"),
                            font=("Arial", 12),
                            bg="#ffffff",
                        )
                    else:
                        khoang = tk.Label(
                            win2,
                            text=("Vô nghiệm"),
                            font=("Arial", 12),
                            bg="#ffffff",
                        )
                elif choose == "<":
                    if a > 0:
                        khoang = tk.Label(
                            win2,
                            text=("Vô nghiệm"),
                            font=("Arial", 12),
                            bg="#ffffff",
                        )
                    else:
                        khoang = tk.Label(
                            win2,
                            text=("Tất cả số thực"),
                            font=("Arial", 12),
                            bg="#ffffff",
                        )
                elif choose == "≥":
                    if a > 0:
                        khoang = tk.Label(
                            win2,
                            text=("Tất cả số thực"),
                            font=("Arial", 12),
                            bg="#ffffff",
                        )
                    else:
                        khoang = tk.Label(
                            win2,
                            text=("Vô nghiệm"),
                            font=("Arial", 12),
                            bg="#ffffff",
                        )
                elif choose == "≤":
                    if a > 0:
                        khoang = tk.Label(
                            win2,
                            text=("Vô nghiệm"),
                            font=("Arial", 12),
                            bg="#ffffff",
                        )
                    else:
                        khoang = tk.Label(
                            win2,
                            text=("Tất cả số thực"),
                            font=("Arial", 12),
                            bg="#ffffff",
                        )
                khoang.place(x=24, y=140)
            elif denta == 0:
                x = -b / (2 * a)
                if choose == ">":
                    if a > 0:
                        khoang = tk.Label(
                            win2,
                            text=(f"x != {x}"),
                            font=("Arial", 12),
                            bg="#ffffff",
                        )
                    else:
                        khoang = tk.Label(
                            win2,
                            text=("Vô nghiệm"),
                            font=("Arial", 12),
                            bg="#ffffff",
                        )
                elif choose == "<":
                    if a > 0:
                        khoang = tk.Label(
                            win2,
                            text=("Vô nghiệm"),
                            font=("Arial", 12),
                            bg="#ffffff",
                        )
                    else:
                        khoang = tk.Label(
                            win2,
                            text=(f"x != {x}"),
                            font=("Arial", 12),
                            bg="#ffffff",
                        )
                elif choose == "≥":
                    if a > 0:
                        khoang = tk.Label(
                            win2,
                            text=("Tất cả số thực"),
                            font=("Arial", 12),
                            bg="#ffffff",
                        )
                    else:
                        khoang = tk.Label(
                            win2,
                            text=(f"x = {x}"),
                            font=("Arial", 12),
                            bg="#ffffff",
                        )
                elif choose == "≤":
                    if a > 0:
                        khoang = tk.Label(
                            win2,
                            text=(f"x = {x}"),
                            font=("Arial", 12),
                            bg="#ffffff",
                        )
                    else:
                        khoang = tk.Label(
                            win2,
                            text=("Tất cả số thực"),
                            font=("Arial", 12),
                            bg="#ffffff",
                        )
                khoang.place(x=24, y=140)
            else:
                sqrt_denta = math.sqrt(denta)
                x1 = round(((-b - sqrt_denta) / (2 * a)), 3)
                x2 = round(((-b + sqrt_denta) / (2 * a)), 3)
                if choose == ">":
                    if a > 0:
                        khoang = tk.Label(
                            win2,
                            text=(f"x < {x1} hoặc x > {x2}"),
                            font=("Arial", 12),
                            bg="#ffffff",
                        )
                    else:
                        khoang = tk.Label(
                            win2,
                            text=(f"{x1} <= x <= {x2}"),
                            font=("Arial", 12),
                            bg="#ffffff",
                        )
                elif choose == "<":
                    if a > 0:
                        khoang = tk.Label(
                            win2,
                            text=(f"{x1} <= x <= {x2}"),
                            font=("Arial", 12),
                            bg="#ffffff",
                        )
                    else:
                        khoang = tk.Label(
                            win2,
                            text=(f"x < {x1} hoặc x > {x2}"),
                            font=("Arial", 12),
                            bg="#ffffff",
                        )
                elif choose == "≥":
                    if a > 0:
                        khoang = tk.Label(
                            win2,
                            text=(f"x <= {x1} hoặc x >= {x2}"),
                            font=("Arial", 12),
                            bg="#ffffff",
                        )
                    else:
                        khoang = tk.Label(
                            win2,
                            text=(f"{x1} <= x <= {x2}"),
                            font=("Arial", 12),
                            bg="#ffffff",
                        )
                elif choose == "≤":
                    if a > 0:
                        khoang = tk.Label(
                            win2,
                            text=(f"{x1} <= x <= {x2}"),
                            font=("Arial", 12),
                            bg="#ffffff",
                        )
                    else:
                        khoang = tk.Label(
                            win2,
                            text=(f"x <= {x2} hoặc x >= {x1}"),
                            font=("Arial", 12),
                            bg="#ffffff",
                        )
                khoang.place(x=24, y=140)
        except:
            alert_box(3)

        # Vẽ đồ thị bất phương trình bậc 2
        x_values = np.arange(-5, 5, 0.1)
        # Tính giá trị y tương ứng với mỗi x
        y_values = a * x_values**2 + b * x_values + c
        # Vẽ đồ thị
        fig, ax = plt.subplots()

        if choose == ">" or choose == "≥":
            if choose == ">":
                plt.plot(
                    x_values, y_values, label=f"{a}x^2 + {b}x + {c} > 0", color="blue"
                )
            elif choose == "≥":
                plt.plot(
                    x_values, y_values, label=f"{a}x^2 + {b}x + {c} >= 0", color="blue"
                )
            plt.fill_between(
                x_values, 0, y_values, where=(y_values > 0), color="gray", alpha=0.3
            )
        if choose == "<" or choose == "≤":

            if choose == "<":
                plt.plot(
                    x_values, y_values, label=f"{a}x^2 + {b}x + {c} < 0", color="blue"
                )
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

        canvas = FigureCanvasTkAgg(fig, master=win2)
        canvas.get_tk_widget().config(width=308, height=230)
        canvas.draw()

        # Hiển thị GUI
        canvas.get_tk_widget().place(x=20, y=180)

        plt.close(fig)

    # Thiết kế giao diện
    text_1 = tk.Label(win2, text=("Nhập hệ số:"), font=("Arial", 12), bg="#ffffff")
    text_1.place(x=20, y=10)

    text_2 = tk.Label(
        win2,
        text=("ax² + bx + c           0  (a ≠ 0)"),
        font=("Arial", 12),
        bg="#ffffff",
    )
    text_2.place(x=60, y=35)

    choose_in = ttk.Combobox(
        win2, font=("Arial", 12), width=1, values=(">", "<", "≥", "≤")
    )
    choose_in.place(x=147, y=36)

    text_input = tk.Label(
        win2,
        text=("a:                       b:                       c:"),
        font=("Arial", 12),
        bg="#ffffff",
    )
    text_input.place(x=20, y=65)

    a_in = tk.Entry(win2, font=("Arial", 12), bg="#f0f0f0", width=8, justify="left")
    a_in.focus()
    a_in.place(x=38, y=69)

    b_in = tk.Entry(win2, font=("Arial", 12), bg="#f0f0f0", width=8, justify="left")
    b_in.place(x=145, y=69)

    c_in = tk.Entry(win2, font=("Arial", 12), bg="#f0f0f0", width=8, justify="left")
    c_in.place(x=250, y=69)

    check_bt = tk.Button(
        win2, text="Giải", font=("Arial", 12), width=6, height=1, command=solve_2
    )
    check_bt.place(x=262, y=28)

    load_khung_2()

    khung_3 = tk.Label(win2, width=43, height=15, bg="#ffffff")
    khung_3.place(x=20, y=180)


# Chương trình con giải hệ phương trình bậc nhất 2 ẩn
def click_hpt_bt():
    win3 = tk.Tk()
    win3.title("Giải hệ phương trình bậc nhất 2 ẩn")
    win3["bg"] = "#344953"
    win3.geometry("350x520")
    win3.resizable(width=False, height=False)
    win3.iconbitmap("image/icon/Calculator_30001.ico")

    khung_1 = tk.Label(win3, width=43, height=10, bg="#ffffff")
    khung_1.place(x=20, y=10)

    def load_khung_2():
        khung_2 = tk.Label(win3, width=43, height=4, bg="#ffffff")
        khung_2.place(x=20, y=180)

    # Hàm tính toán
    def solve_3():

        load_khung_2()

        try:
            a1 = float(a1_in.get())
            a2 = float(a2_in.get())
            b1 = float(b1_in.get())
            b2 = float(b2_in.get())
            c1 = float(c1_in.get())
            c2 = float(c2_in.get())
        except:
            alert_box(2)

        try:
            x = ((b2 * c1) - (b1 * c2)) / ((a1 * b2) - (a2 * b1))
            y = ((a1 * c2) - (a2 * c1)) / ((a1 * b2) - (a2 * b1))

            x_out = tk.Label(
                win3, text="  x = " + str(x), font=("Arial", 12), bg="#ffffff"
            )
            x_out.place(x=25, y=185)

            y_out = tk.Label(
                win3, text="  y = " + str(y), font=("Arial", 12), bg="#ffffff"
            )
            y_out.place(x=25, y=215)
        except:
            rong_out = tk.Label(
                win3,
                text=("=> Hệ phương trình vô nghiệm"),
                font=("Arial", 12),
                bg="#ffffff",
            )
            rong_out.place(x=25, y=200)
        # Vẽ đồ thị hệ phương trình bậc nhất 2 ẩn
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

        canvas = FigureCanvasTkAgg(fig, master=win3)
        canvas.get_tk_widget().config(width=308, height=230)
        canvas.draw()

        # Hiển thị GUI
        canvas.get_tk_widget().place(x=20, y=260)

        plt.close(fig)

    # Thiết kế giao diện
    text_1 = tk.Label(win3, text=("Nhập hệ số:"), font=("Arial", 12), bg="#ffffff")
    text_1.place(x=20, y=10)

    text_2 = tk.Label(win3, text=("{"), font=("Times New Roman", 34), bg="#ffffff")
    text_2.place(x=60, y=35)

    text_2a = tk.Label(
        win3, text=("a₁x  +  b₁y  =  c₁"), font=("Times New Roman", 16), bg="#ffffff"
    )
    text_2a.place(x=85, y=40)
    text_2b = tk.Label(
        win3, text=("a₂x  +  b₂y  =  c₂"), font=("Times New Roman", 16), bg="#ffffff"
    )
    text_2b.place(x=85, y=65)

    text_input_1 = tk.Label(
        win3,
        text=("a₁:                 b₁:                c₁:"),
        font=("Times New Roman", 14),
        bg="#ffffff",
    )
    text_input_1.place(x=20, y=105)

    text_input_2 = tk.Label(
        win3,
        text=("a₂:                 b₂:                c₂:"),
        font=("Times New Roman", 14),
        bg="#ffffff",
    )
    text_input_2.place(x=20, y=135)

    a1_in = tk.Entry(win3, font=("Arial", 12), bg="#f0f0f0", width=8, justify="left")
    a1_in.focus()
    a1_in.place(x=44, y=110)

    a2_in = tk.Entry(win3, font=("Arial", 12), bg="#f0f0f0", width=8, justify="left")
    a2_in.place(x=44, y=140)

    b1_in = tk.Entry(win3, font=("Arial", 12), bg="#f0f0f0", width=8, justify="left")
    b1_in.place(x=148, y=110)

    b2_in = tk.Entry(win3, font=("Arial", 12), bg="#f0f0f0", width=8, justify="left")
    b2_in.place(x=148, y=140)

    c1_in = tk.Entry(win3, font=("Arial", 12), bg="#f0f0f0", width=8, justify="left")
    c1_in.place(x=250, y=110)

    c2_in = tk.Entry(win3, font=("Arial", 12), bg="#f0f0f0", width=8, justify="left")
    c2_in.place(x=250, y=140)

    check_bt = tk.Button(
        win3, text="Giải", font=("Arial", 12), width=6, height=1, command=solve_3
    )
    check_bt.place(x=262, y=55)

    load_khung_2()

    khung_3 = tk.Label(win3, width=43, height=15, bg="#ffffff")
    khung_3.place(x=20, y=260)


# Nút chạy phương trình bậc 2
pt_bt = tk.Button(
    win,
    text="Phương trình bậc 2",
    font=("Arial", 12),
    width=30,
    height=1,
    bg="#344953",
    fg="#ffffff",
    command=click_pt_bt,
)
pt_bt.place(x=35, y=25)

# Nút chạy bất phương trình bậc 2
bpt_bt = tk.Button(
    win,
    text="Bất phương trình bậc 2",
    font=("Arial", 12),
    width=30,
    height=1,
    bg="#344953",
    fg="#ffffff",
    command=click_bpt_bt,
)
bpt_bt.place(x=35, y=65)

# Nút chạy hệ phương trình bậc nhất 2 ẩn
hpt_bt = tk.Button(
    win,
    text="Hệ phương trình bậc nhất 2 ẩn",
    font=("Arial", 12),
    width=30,
    height=1,
    bg="#344953",
    fg="#ffffff",
    command=click_hpt_bt,
)
hpt_bt.place(x=35, y=105)

tk.mainloop()
