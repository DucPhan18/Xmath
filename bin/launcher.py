import tkinter as tk
from tkinter import ttk

import feature
import pt
import bpt
import hpt


win = tk.Tk()
win.title("X math")
win.geometry("350x160")
win.resizable(width=False, height=False)
win.attributes("-topmost", True)
win.iconbitmap("image/icon/Calculator_30001.ico")
feature.center_window(win)


def khung(master, width, height, bg, x, y):
    khung = tk.Label(master, width=width, height=height, bg=bg)
    khung.place(x=x, y=y)


# Chương trình con giải phương trình bậc 2
def pt_b2_bt():
    win1 = tk.Tk()
    win1.title("Giải phương trình bậc 2")
    win1["bg"] = "#344953"
    win1.geometry("350x440")
    win1.resizable(width=False, height=False)
    win1.iconbitmap("image/icon/Calculator_30001.ico")

    khung(win1, 43, 5, "#ffffff", 20, 10)

    # Hàm tính toán
    def solve_1():
        khung(win1, 43, 4, "#ffffff", 20, 103)
        try:
            a = float(a_in.get())
            b = float(b_in.get())
            c = float(c_in.get())
        except:
            feature.alert_box(2)
        pt.pt_b2(win1, a, b, c)

        # Vẽ đồ thị phương trình bậc 2
        feature.graph_1(win1, a, b, c)

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
    khung(win1, 43, 4, "#ffffff", 20, 103)
    khung(win1, 43, 15, "#ffffff", 20, 180)


# Chương trình con giải bất phương trình bậc 2
def click_bpt_bt():
    win2 = tk.Tk()
    win2.title("Giải bất phương trình bậc 2")
    win2["bg"] = "#344953"
    win2.geometry("350x440")
    win2.resizable(width=False, height=False)
    win2.iconbitmap("image/icon/Calculator_30001.ico")

    khung(win2, 43, 5, "#ffffff", 20, 10)

    # Hàm tính toán
    def solve_2():

        khung(win2, 43, 4, "#ffffff", 20, 103)

        try:
            a = float(a_in.get())
            b = float(b_in.get())
            c = float(c_in.get())
        except:
            feature.alert_box(2)

        choose = str(choose_in.get())

        bpt.bpt_b2(win2, a, b, c, choose)

        # Vẽ đồ thị bất phương trình bậc 2
        feature.graph_2(win2, a, b, c, choose)

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

    khung(win2, 43, 4, "#ffffff", 20, 103)

    khung(win2, 43, 15, "#ffffff", 20, 180)


# Chương trình con giải hệ phương trình bậc nhất 2 ẩn
def click_hpt_bt():
    win3 = tk.Tk()
    win3.title("Giải hệ phương trình bậc nhất 2 ẩn")
    win3["bg"] = "#344953"
    win3.geometry("350x520")
    win3.resizable(width=False, height=False)
    win3.iconbitmap("image/icon/Calculator_30001.ico")

    khung(win3, 43, 10, "#ffffff", 20, 10)

    # Hàm tính toán
    def solve_3():

        khung(win3, 43, 4, "#ffffff", 20, 180)

        try:
            a1 = float(a1_in.get())
            a2 = float(a2_in.get())
            b1 = float(b1_in.get())
            b2 = float(b2_in.get())
            c1 = float(c1_in.get())
            c2 = float(c2_in.get())
        except:
            feature.alert_box(2)

        hpt.hpt_b1_2an(win3, a1, a2, b1, b2, c1, c2)

        # Vẽ đồ thị hệ phương trình bậc nhất 2 ẩn
        feature.graph_3(win3, a1, a2, b1, b2, c1, c2)

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

    khung(win3, 43, 4, "#ffffff", 20, 180)

    khung(win3, 43, 15, "#ffffff", 20, 260)


# Nút chạy phương trình bậc 2
pt_bt = tk.Button(
    win,
    text="Phương trình bậc 2",
    font=("Arial", 12),
    width=30,
    height=1,
    bg="#344953",
    fg="#ffffff",
    command=pt_b2_bt,
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
