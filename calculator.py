import tkinter as tk


class Calculator:
    def __init__(self) -> None:
        self.calculation = ""
        self.root = tk.Tk()
        self.root.title("Calculator")
        self.root.geometry("300x275")
        self.result_box = tk.Text(self.root, height=2, font=("Arial", 18), width=21)
        self.result_box.grid(columnspan=5, padx=10)
        self.btn1 = tk.Button(
            self.root,
            width=5,
            text="1",
            command=lambda: self.add_to_calculation(1),
            font=("Arial", 14),
        )
        self.btn1.grid(row=2, column=1)
        self.btn2 = tk.Button(
            self.root,
            width=5,
            text="2",
            command=lambda: self.add_to_calculation(2),
            font=("Arial", 14),
        )
        self.btn2.grid(row=2, column=2)
        self.btn3 = tk.Button(
            self.root,
            width=5,
            text="3",
            command=lambda: self.add_to_calculation(3),
            font=("Arial", 14),
        )
        self.btn3.grid(row=2, column=3)
        self.btn4 = tk.Button(
            self.root,
            width=5,
            text="4",
            command=lambda: self.add_to_calculation(4),
            font=("Arial", 14),
        )
        self.btn4.grid(row=3, column=1)
        self.btn5 = tk.Button(
            self.root,
            width=5,
            text="5",
            command=lambda: self.add_to_calculation(5),
            font=("Arial", 14),
        )
        self.btn5.grid(row=3, column=2)
        self.btn6 = tk.Button(
            self.root,
            width=5,
            text="6",
            command=lambda: self.add_to_calculation(6),
            font=("Arial", 14),
        )
        self.btn6.grid(row=3, column=3)
        self.btn7 = tk.Button(
            self.root,
            width=5,
            text="7",
            command=lambda: self.add_to_calculation(7),
            font=("Arial", 14),
        )
        self.btn7.grid(row=4, column=1)
        self.btn8 = tk.Button(
            self.root,
            width=5,
            text="8",
            command=lambda: self.add_to_calculation(8),
            font=("Arial", 14),
        )
        self.btn8.grid(row=4, column=2)
        self.btn9 = tk.Button(
            self.root,
            width=5,
            text="9",
            command=lambda: self.add_to_calculation(9),
            font=("Arial", 14),
        )
        self.btn9.grid(row=4, column=3)
        self.btn0 = tk.Button(
            self.root,
            width=5,
            text="0",
            command=lambda: self.add_to_calculation(0),
            font=("Arial", 14),
        )
        self.btn0.grid(row=5, column=1)
        self.btn_plus = tk.Button(
            self.root,
            width=5,
            text="+",
            command=lambda: self.add_to_calculation("+"),
            font=("Arial", 14),
        )
        self.btn_plus.grid(row=2, column=4)
        self.btn_minus = tk.Button(
            self.root,
            width=5,
            text="-",
            command=lambda: self.add_to_calculation("-"),
            font=("Arial", 14),
        )
        self.btn_minus.grid(row=3, column=4)
        self.btn_mul = tk.Button(
            self.root,
            width=5,
            text="x",
            command=lambda: self.add_to_calculation("*"),
            font=("Arial", 14),
        )
        self.btn_mul.grid(row=4, column=4)
        self.btn_div = tk.Button(
            self.root,
            width=5,
            text="/",
            command=lambda: self.add_to_calculation("/"),
            font=("Arial", 14),
        )
        self.btn_div.grid(row=5, column=4)
        self.btn_open = tk.Button(
            self.root,
            width=5,
            text="(",
            command=lambda: self.add_to_calculation("("),
            font=("Arial", 14),
        )
        self.btn_open.grid(row=5, column=2)
        self.btn_close = tk.Button(
            self.root,
            width=5,
            text=")",
            command=lambda: self.add_to_calculation(")"),
            font=("Arial", 14),
        )
        self.btn_close.grid(row=5, column=3)
        self.btn_clear = tk.Button(
            self.root,
            width=11,
            text="C",
            command=self.clear_field,
            font=("Arial", 14),
        )
        self.btn_clear.grid(row=6, column=1, columnspan=2)
        self.btn_equals = tk.Button(
            self.root,
            width=11,
            text="=",
            command=self.evaluate_calculation,
            font=("Arial", 14),
        )
        self.btn_equals.grid(row=6, column=3, columnspan=2)
        self.root.mainloop()

    def add_to_calculation(self, symbol):
        self.calculation += str(symbol)
        self.result_box.delete(1.0, "end")
        self.result_box.insert(1.0, self.calculation)

    def evaluate_calculation(self):
        try:
            result = str(eval(self.calculation))
            self.calculation = ""
            self.result_box.delete(1.0, "end")
            self.result_box.insert(1.0, result)
        except:
            self.clear_field()
            self.result_box.insert(1.0, "ERROR")

    def clear_field(self):
        self.calculation = ""
        self.result_box.delete(1, 0, "end")


Calculator()
