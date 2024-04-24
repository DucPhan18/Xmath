import tkinter as tk
import math
import feature


def bpt_b2(master, a, b, c, d, choose):
    if a == 0:
        feature.alert_box(1)
    denta = pow(b, 2) - (4 * a * c)
    denta_out = tk.Label(
        master, text=" Δ = " + str(denta), font=("Arial", 12), bg="#ffffff"
    )
    denta_out.place(x=20, y=105)
    try:
        if denta < 0:
            if choose == ">":
                if a > 0:
                    khoang = tk.Label(
                        master,
                        text=("Tất cả số thực"),
                        font=("Arial", 12),
                        bg="#ffffff",
                    )
                else:
                    khoang = tk.Label(
                        master,
                        text=("Vô nghiệm"),
                        font=("Arial", 12),
                        bg="#ffffff",
                    )
            elif choose == "<":
                if a > 0:
                    khoang = tk.Label(
                        master,
                        text=("Vô nghiệm"),
                        font=("Arial", 12),
                        bg="#ffffff",
                    )
                else:
                    khoang = tk.Label(
                        master,
                        text=("Tất cả số thực"),
                        font=("Arial", 12),
                        bg="#ffffff",
                    )
            elif choose == "≥":
                if a > 0:
                    khoang = tk.Label(
                        master,
                        text=("Tất cả số thực"),
                        font=("Arial", 12),
                        bg="#ffffff",
                    )
                else:
                    khoang = tk.Label(
                        master,
                        text=("Vô nghiệm"),
                        font=("Arial", 12),
                        bg="#ffffff",
                    )
            elif choose == "≤":
                if a > 0:
                    khoang = tk.Label(
                        master,
                        text=("Vô nghiệm"),
                        font=("Arial", 12),
                        bg="#ffffff",
                    )
                else:
                    khoang = tk.Label(
                        master,
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
                        master,
                        text=(f"x != {x}"),
                        font=("Arial", 12),
                        bg="#ffffff",
                    )
                else:
                    khoang = tk.Label(
                        master,
                        text=("Vô nghiệm"),
                        font=("Arial", 12),
                        bg="#ffffff",
                    )
            elif choose == "<":
                if a > 0:
                    khoang = tk.Label(
                        master,
                        text=("Vô nghiệm"),
                        font=("Arial", 12),
                        bg="#ffffff",
                    )
                else:
                    khoang = tk.Label(
                        master,
                        text=(f"x != {x}"),
                        font=("Arial", 12),
                        bg="#ffffff",
                    )
            elif choose == "≥":
                if a > 0:
                    khoang = tk.Label(
                        master,
                        text=("Tất cả số thực"),
                        font=("Arial", 12),
                        bg="#ffffff",
                    )
                else:
                    khoang = tk.Label(
                        master,
                        text=(f"x = {x}"),
                        font=("Arial", 12),
                        bg="#ffffff",
                    )
            elif choose == "≤":
                if a > 0:
                    khoang = tk.Label(
                        master,
                        text=(f"x = {x}"),
                        font=("Arial", 12),
                        bg="#ffffff",
                    )
                else:
                    khoang = tk.Label(
                        master,
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
                        master,
                        text=(f"x < {x1} hoặc x > {x2}"),
                        font=("Arial", 12),
                        bg="#ffffff",
                    )
                else:
                    khoang = tk.Label(
                        master,
                        text=(f"{x1} <= x <= {x2}"),
                        font=("Arial", 12),
                        bg="#ffffff",
                    )
            elif choose == "<":
                if a > 0:
                    khoang = tk.Label(
                        master,
                        text=(f"{x1} <= x <= {x2}"),
                        font=("Arial", 12),
                        bg="#ffffff",
                    )
                else:
                    khoang = tk.Label(
                        master,
                        text=(f"x < {x1} hoặc x > {x2}"),
                        font=("Arial", 12),
                        bg="#ffffff",
                    )
            elif choose == "≥":
                if a > 0:
                    khoang = tk.Label(
                        master,
                        text=(f"x <= {x1} hoặc x >= {x2}"),
                        font=("Arial", 12),
                        bg="#ffffff",
                    )
                else:
                    khoang = tk.Label(
                        master,
                        text=(f"{x1} <= x <= {x2}"),
                        font=("Arial", 12),
                        bg="#ffffff",
                    )
            elif choose == "≤":
                if a > 0:
                    khoang = tk.Label(
                        master,
                        text=(f"{x1} <= x <= {x2}"),
                        font=("Arial", 12),
                        bg="#ffffff",
                    )
                else:
                    khoang = tk.Label(
                        master,
                        text=(f"x <= {x2} hoặc x >= {x1}"),
                        font=("Arial", 12),
                        bg="#ffffff",
                    )
            khoang.place(x=24, y=140)
    except:
        feature.alert_box(3)
