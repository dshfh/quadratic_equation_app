import tkinter as tk
from tkinter import ttk, messagebox

from quadratic_solver import solve_quadratic
from validator import is_valid_number
from formatter import format_number, create_solution_text

class QuadraticEquationApp:

    def __init__(self, root):
        self.validate_number = None
        self.root = root

        self.root.title(
            "Quadratic Equation Learning Tool"
        )

        self.root.geometry("1000x750")
        self.root.minsize(850, 650)

        self.setup_styles()
        self.create_numeric_validation()
        self.create_interface()

    def setup_styles(self):
        style = ttk.Style()

        style.configure(
            "Title.TLabel",
            font=("Arial", 20, "bold")
        )

        style.configure(
            "Heading.TLabel",
            font=("Arial", 14, "bold")
        )

        style.configure(
            "Normal.TLabel",
            font=("Arial", 14)
        )

        style.configure(
            "Result.TLabel",
            font=("Arial", 14)
        )

        style.configure(
            "Solve.TButton",
            font=("Arial", 14, "bold"),
            padding=8
        )

        style.configure(
            "Clear.TButton",
            font=("Arial", 14),
            padding=8
        )

    def create_numeric_validation(self):
        self.validate_number = self.root.register(
            self.validate_input
        )

    def validate_input(self, value):
        if is_valid_number(value):
            return True

        messagebox.showwarning(
            "Input Error",
            'Only numeric values and the signs "-" and "." are allowed.'
        )

        return False

    def create_interface(self):
        # Main container
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(fill="both", expand=True)


        # Title
        title = ttk.Label(
            main_frame,
            text="Quadratic Equation Learning Tool",
            style="Title.TLabel"
        )
        title.pack(pady=(0, 15))


        # Main horizontal container
        content_frame = ttk.Frame(main_frame)
        content_frame.pack(fill="both", expand=True)


        # =========================================================
        # LEFT SIDE - THEORY
        # =========================================================


        theory_frame = ttk.LabelFrame(
            content_frame,
            text="Theory",
            padding=15
        )
        content_frame.columnconfigure(0, weight=3)
        content_frame.columnconfigure(1, weight=7)
        content_frame.rowconfigure(0, weight=1)


        theory_frame.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 10)
        )

        with open("theory.txt", "r", encoding="utf-8") as file:
            theory_text = file.read()

        theory_scroll = tk.Scrollbar(theory_frame)
        theory_scroll.pack(side="right", fill="y")


        theory_box = tk.Text(
            theory_frame,
            wrap="word",
            font=("Arial", 11),
            bg="white",
            relief="flat",
            padx=10,
            pady=10,
            yscrollcommand=theory_scroll.set
        )
        theory_box.pack(fill="both", expand=True)


        theory_scroll.config(command=theory_box.yview)


        theory_box.insert("1.0", theory_text)
        theory_box.config(state="disabled")


        # =========================================================
        # RIGHT SIDE - CALCULATOR
        # =========================================================


        calculator_frame = ttk.Frame(content_frame)


        calculator_frame.grid(
            row=0,
            column=1,
            sticky="nsew"
        )


        # Input section
        input_frame = ttk.LabelFrame(
            calculator_frame,
            text="Equation Coefficients",
            padding=15
        )
        input_frame.pack(fill="x", pady=(0, 10))


        ttk.Label(
            input_frame,
            text="For equation: ax² + bx + c = 0",
            style="Heading.TLabel"
        ).grid(
            row=0,
            column=0,
            columnspan=2,
            pady=(0, 15)
        )


        # Variables
        ttk.Label(
            input_frame,
            text="a:"
        ).grid(row=1, column=0, sticky="w", pady=5)


        self.a_entry = ttk.Entry(
            input_frame,
            width=20,
            validate="key",
            validatecommand=(self.validate_number, "%P")
        )
        self.a_entry.grid(row=1, column=1, sticky="ew", pady=5)


        ttk.Label(
            input_frame,
            text="b:"
        ).grid(row=2, column=0, sticky="w", pady=5)


        self.b_entry = ttk.Entry(
            input_frame,
            width=20,
            validate="key",
            validatecommand=(self.validate_number, "%P")
        )
        self.b_entry.grid(row=2, column=1, sticky="ew", pady=5)


        ttk.Label(
            input_frame,
            text="c:"
        ).grid(row=3, column=0, sticky="w", pady=5)


        self.c_entry = ttk.Entry(
            input_frame,
            width=20,
            validate="key",
            validatecommand=(self.validate_number, "%P")
        )
        self.c_entry.grid(row=3, column=1, sticky="ew", pady=5)


        input_frame.columnconfigure(1, weight=1)


        # Buttons
        button_frame = ttk.Frame(calculator_frame)
        button_frame.pack(fill="x", pady=(0, 10))


        solve_button = ttk.Button(
            button_frame,
            text="Solve",
            style="Solve.TButton",
            command=self.solve_equation
        )
        solve_button.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(0, 5)
        )


        clear_button = ttk.Button(
            button_frame,
            text="Clear Fields",
            style="Clear.TButton",
            command=self.clear_fields
        )
        clear_button.pack(
            side="right",
            fill="x",
            expand=True,
            padx=(5, 0)
        )


        # Result section
        result_frame = ttk.LabelFrame(
            calculator_frame,
            text="Solution",
            padding=10
        )
        result_frame.pack(
            fill="both",
            expand=True
        )


        result_scroll = tk.Scrollbar(result_frame)
        result_scroll.pack(side="right", fill="y")


        self.result_text = tk.Text(
            result_frame,
            wrap="word",
            font=("Consolas", 10),
            bg="white",
            padx=10,
            pady=10,
            yscrollcommand=result_scroll.set
        )
        self.result_text.pack(
            fill="both",
            expand=True
        )


        result_scroll.config(
            command=self.result_text.yview
        )


        self.result_text.insert(
            "1.0",
            "Enter the coefficients a, b and c, then click \"Solve\"."
        )


        self.result_text.config(state="disabled")

    def set_result(self, text):
        self.result_text.config(state="normal")
        self.result_text.delete("1.0", tk.END)
        self.result_text.insert("1.0", text)
        self.result_text.config(state="disabled")

    def solve_equation(self):

        if (
                not self.a_entry.get().strip()
                or not self.b_entry.get().strip()
                or not self.c_entry.get().strip()
        ):
            messagebox.showwarning(
                "Input Error",
                "Please enter values for a, b and c."
            )
            return

        try:
            a = float(self.a_entry.get())
            b = float(self.b_entry.get())
            c = float(self.c_entry.get())

        except ValueError:
            messagebox.showerror(
                "Input Error",
                "Only numeric values are allowed."
            )
            return

        if a == 0:
            messagebox.showerror(
                "Input Error",
                "The coefficient 'a' cannot be zero."
            )
            return

        result = solve_quadratic(a, b, c)

        solution = create_solution_text(
            a,
            b,
            c,
            result
        )

        self.set_result(solution)

    def clear_fields(self):
        self.a_entry.delete(0, tk.END)
        self.b_entry.delete(0, tk.END)
        self.c_entry.delete(0, tk.END)

        self.set_result(
            "Enter the coefficients a, b and c, "
            "then click \"Solve\"."
        )

        self.a_entry.focus()