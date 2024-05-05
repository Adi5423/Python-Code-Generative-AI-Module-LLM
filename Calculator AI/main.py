import operator as op
import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("400x300")

        self.result = 0
        self.current_operation = None
        self.current_input = ""

        self.create_widgets()

    def create_widgets(self):
        self.display = tk.Entry(self, text="", width=20)
        self.display.grid(row=0, column=0, columnspan=4)

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3),
            ("(", 5, 0), (")", 5, 1), ("^", 5, 2), ("%", 5, 3),
        ]

        for (text, row, column) in buttons:
            button = tk.Button(self, text=text, width=5, height=2, command=lambda t=text: self.button_click(t))
            button.grid(row=row, column=column)

        self.equals_button = tk.Button(self, text="=", width=5, height=2, command=self.calculate)
        self.equals_button.grid(row=5, column=3)

    def button_click(self, text):
        if text == "C":
            self.display.delete(0, tk.END)
            self.result = 0
            self.current_operation = None
            self.current_input = ""
        elif text == "(":
            self.current_input += "("
        elif text == ")":
            self.current_input += ")"
        elif text == "^":
            self.current_input += "**"
        elif text == "%":
            self.current_input += "/100"
        else:
            self.current_input += text
            self.display.insert(tk.END, text)

    def calculate(self):
        if self.current_operation:
            result = self.current_operation(self.result, float(self.current_input))
        else:
            result = float(self.current_input)

        self.display.delete(0, tk.END)
        self.display.insert(tk.END, str(result))
        self.result = result
        self.current_operation = None
        self.current_input = ""

def main():
    calculator = Calculator()
    calculator.mainloop()

if __name__ == "__main__":
    main()