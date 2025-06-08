import tkinter as tk
from tkinter import messagebox


class Calcutrice:
    def __init__(self, root):
        self.root = root
        self.root.title("Calcutrice In Python")
        self.root.configure(bg="#2b2b2b")
        self.root.geometry("375x550")
        self.root.resizable(False, False)

        self.entryp = tk.Entry(
            root,
            width=17,
            font=("Helvetica", 26),
            borderwidth=0,
            relief="solid",
            bg="#2b2b2b",
            fg="white",
            justify="right",
        )
        self.entryp.grid(
            row=0, column=0, columnspan=1, ipadx=0, ipady=1, padx=(1, 2), pady=(1, 10)
        )

        self.butom_created()

    def butom_created(self):
        butoms = [
            ("C", 2),
            ("←", 1),
            ("/", 1),
            ("7", 1),
            ("8", 1),
            ("9", 1),
            ("*", 1),
            ("4", 1),
            ("5", 1),
            ("6", 1),
            ("-", 1),
            ("1", 1),
            ("2", 1),
            ("3", 1),
            ("+", 1),
            ("0", 2),
            (".", 1),
            ("=", 1),
        ]
        
        color_butoms = {
            "number": "#4d4d4d",
            "operator": "#fe9505",
            "equal": "#fe9505",
            "background": "#2b2b2b",
            "text": "#ffffff",
            "reset": "#d32f2f",
            "delete": "#fe9505",
        }

        frame_butoms = tk.Frame(self.root, bg="#2b2b2b")
        frame_butoms.grid(row=1, column=0, columnspan=4, pady=(0, 10))

        row1 = 0
        column1 = 0
        
        
        for butom, span in butoms:
            color_background = (
                color_butoms["operator"]
                if butom in ["/", "*", "-", "+", "=", "<-"]
                else color_butoms["number"]
            )
            if butom == "C":
                color_background = color_butoms["reset"]
            elif butom == "←":
                color_background = color_butoms["delete"]
            elif butom == "=":
                color_background = color_butoms["equal"]

            tk.Button(
                frame_butoms,
                text=butom,
                width=5 * span,
                height=2,
                font=("Arial", 20),
                bg=color_background,
                fg=color_butoms["text"],
                borderwidth=0,
                command=lambda b=butom: self.click_butom(b),
            ).grid(
                row=row1, column=column1, columnspan=span, padx=1, pady=1, sticky="nsew"
            )

            column1 += span
            if column1 >= 4:
                row1 += 1
                column1 = 0

    def validentry(self, expretion):
        operators = set("+-*/")
        for i in range(1, len(expretion)):
            if expretion[i] in operators and expretion[i - 1] in operators:
                return False
        return True

    def click_butom(self, value):
        if value == "=":
            expretion = self.entryp.get()
            if self.validentry(expretion):
                try:
                    resultado = str(eval(expretion))
                    self.entryp.delete(0, tk.END)
                    self.entryp.insert(tk.END, resultado)
                except Exception:
                    messagebox.showerror("ERROR", "Invalid Entry.")
                    self.entryp.delete(0, tk.END)
            else:
                messagebox.showerror("ERROR", "Consecutive Operators Not Allowed.")
        elif value == "C":
            self.entryp.delete(0, tk.END)
        elif value == "←":
            if len(self.entryp.get()) > 0:
                self.entryp.delete(len(self.entryp.get()) - 1, tk.END)
        else:
            self.entryp.insert(tk.END, value)


if __name__ == "__main__":
    root = tk.Tk()
    calcutrice = Calcutrice(root)
    root.mainloop()

