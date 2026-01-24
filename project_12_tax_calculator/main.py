import customtkinter as ctk


class TaxCalculator:
    def __init__(self):
        # Initialize our window
        self.window = ctk.CTk()
        self.window.title("Tax Calculator")
        self.window.geometry("280x200")
        self.window.resizable(False, False)

        self.padding: dict = {"padx": 20, "pady": 10}

        # Income label
        self.income_label = ctk.CTkLabel(self.window, text="Income:")
        # The ** operator unpacks a dictionary into keyword arguments.
        # (like spread operator in TS)
        self.income_label.grid(row=0, column=0, **self.padding)

        # Income input field
        self.income_entry = ctk.CTkEntry(self.window)
        self.income_entry.grid(row=0, column=1, **self.padding)

        # Tax rate label
        self.tax_rate_label = ctk.CTkLabel(self.window, text="Percent:")
        self.tax_rate_label.grid(row=1, column=0, **self.padding)

        # Tax rate input field
        self.tax_rate_entry = ctk.CTkEntry(self.window)
        self.tax_rate_entry.grid(row=1, column=1, **self.padding)

        # Result label
        self.result_label = ctk.CTkLabel(self.window, text="Tax:")
        self.result_label.grid(row=2, column=0, **self.padding)

        # Result input field
        self.result_entry = ctk.CTkEntry(self.window)
        self.result_entry.insert(0, "0")  # Default value
        self.result_entry.grid(row=2, column=1, **self.padding)

        # Calculate button
        self.calculate = ctk.CTkButton(
            self.window, text="Calculate", command=self.calculate_tax
        )
        self.calculate.grid(row=3, column=1, **self.padding)

    def update_result(self, text: str):
        self.result_entry.delete(0, ctk.END)
        self.result_entry.insert(0, text)

    def calculate_tax(self):
        try:
            income: float = float(self.income_entry.get())
            tax_rate: float = float(self.tax_rate_entry.get())

            self.update_result(f"£{(income * tax_rate / 100):,.2f}")
        except:
            self.update_result("Invalid value")

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    tc = TaxCalculator()
    tc.run()
