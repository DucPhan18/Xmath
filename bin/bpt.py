import tkinter as tk
import math
import feature


def bpt_b2(master, a, b, c, choose):
    if a == 0:
        feature.alert_box(1)
    denta = pow(b, 2) - (4 * a * c)
    denta_out = tk.Label(
        master, text=" Δ = " + str(denta), font=("Arial", 12), bg="#ffffff"
    )
    denta_out.place(x=20, y=105)
    try:
       pass
    except:
        feature.alert_box(3)
