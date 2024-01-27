import tkinter as tk


def clear_field():
    global calculation

    calculation = ""
    result_box.delete(1.0, "end")


def evaluate_calculation():
    global calculation
    try:
        result = str(eval(calculation))
        calculation = ""
        result_box.delete(1.0, "end")
        result_box.insert(1.0, result)
    except:
        clear_field()
        result_box.insert(1.0, "ERROR")


def add_to_calculation(symbol):
    global calculation

    calculation += str(symbol)
    result_box.delete(1.0, "end")
    result_box.insert(1.0, calculation)


controls = [
    {"text": "1", "command": lambda: add_to_calculation("1"), "row": 2, "column": 1},
    {"text": "2", "command": lambda: add_to_calculation("2"), "row": 2, "column": 2},
    {"text": "3", "command": lambda: add_to_calculation("3"), "row": 2, "column": 3},
    {"text": "4", "command": lambda: add_to_calculation("4"), "row": 3, "column": 1},
    {"text": "5", "command": lambda: add_to_calculation("5"), "row": 3, "column": 2},
    {"text": "6", "command": lambda: add_to_calculation("6"), "row": 3, "column": 3},
    {"text": "7", "command": lambda: add_to_calculation("7"), "row": 4, "column": 1},
    {"text": "8", "command": lambda: add_to_calculation("8"), "row": 4, "column": 2},
    {"text": "9", "command": lambda: add_to_calculation("9"), "row": 4, "column": 3},
    {"text": "0", "command": lambda: add_to_calculation("0"), "row": 5, "column": 1},
    {"text": "+", "command": lambda: add_to_calculation("+"), "row": 2, "column": 4},
    {"text": "-", "command": lambda: add_to_calculation("-"), "row": 3, "column": 4},
    {"text": "*", "command": lambda: add_to_calculation("*"), "row": 4, "column": 4},
    {"text": "(", "command": lambda: add_to_calculation("("), "row": 5, "column": 2},
    {"text": ")", "command": lambda: add_to_calculation(")"), "row": 5, "column": 3},
    {"text": "/", "command": lambda: add_to_calculation("/"), "row": 5, "column": 4},
    {
        "text": "C",
        "command": clear_field,
        "row": 6,
        "column": 1,
        "colspan": 2,
        "width": 11,
    },
    {
        "text": "=",
        "command": evaluate_calculation,
        "row": 6,
        "column": 3,
        "colspan": 2,
        "width": 11,
    },
]


calculation = ""
root = tk.Tk()
root.title("Calculator")
root.geometry("300x275")
result_box = tk.Text(root, height=2, font=("Arial", 18), width=21)
result_box.grid(columnspan=5, padx=10)


for control in controls:
    ui_control = tk.Button(
        root,
        width=control.get("width", 5),
        text=control["text"],
        command=control["command"],
        font=("Arial", 14),
    )
    ui_control.grid(
        row=control["row"],
        column=control["column"],
        columnspan=control.get("colspan", 1),
    )
root.mainloop()
