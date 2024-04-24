import tkinter as tk


def hpt_b1_2an(master, a1, a2, b1, b2, c1, c2):
    try:
        x = ((b2 * c1) - (b1 * c2)) / ((a1 * b2) - (a2 * b1))
        y = ((a1 * c2) - (a2 * c1)) / ((a1 * b2) - (a2 * b1))
        x_out = tk.Label(
            master, text="  x = " + str(x), font=("Arial", 12), bg="#ffffff"
        )
        x_out.place(x=25, y=185)
        y_out = tk.Label(
            master, text="  y = " + str(y), font=("Arial", 12), bg="#ffffff"
        )
        y_out.place(x=25, y=215)
    except:
        rong_out = tk.Label(
            master,
            text=("=> Hệ phương trình vô nghiệm"),
            font=("Arial", 12),
            bg="#ffffff",
        )
        rong_out.place(x=25, y=200)
