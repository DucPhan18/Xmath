import tkinter as tk
import math
import feature


def pt_b2(master, a, b, c):
    if a == 0:
        feature.alert_box(1)
    denta = pow(b, 2) - (4 * a * c)
    denta_out = tk.Label(
        master, text="  Δ = " + str(denta), font=("Arial", 12), bg="#ffffff"
    )
    denta_out.place(x=20, y=105)
    if denta > 0:
        can_denta = float(math.sqrt(denta))
        x1 = float((-b + can_denta) / (2 * a))
        x2 = float((-b - can_denta) / (2 * a))
        x1_out = tk.Label(
            master, text="  x1 = " + str(x1), font=("Arial", 12), bg="#ffffff"
        )
        x1_out.place(x=20, y=125)
        x2_out = tk.Label(
            master, text="  x2 = " + str(x2), font=("Arial", 12), bg="#ffffff"
        )
        x2_out.place(x=20, y=145)
    elif denta == 0:
        x = x1 = x2 = -b / (2 * a)
        x_out = tk.Label(
            master, text="  x = " + str(x), font=("Arial", 12), bg="#ffffff"
        )
        x_out.place(x=20, y=125)
    else:
        rong_out = tk.Label(
            master,
            text="Vô nghiệm",
            font=("Arial", 12),
            bg="#ffffff",
        )
        rong_out.place(x=20, y=145)
