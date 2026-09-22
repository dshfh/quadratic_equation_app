import tkinter as tk

from gui import QuadraticEquationApp


def main():
    root = tk.Tk()
    app = QuadraticEquationApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()