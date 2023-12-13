import tkinter as tk
from tkinter import messagebox

class PizzaOrder:
    def __init__(self, master):
        self.master = master
        master.title("Tasty Pizza Order Form")

        # Create input labels and entry boxes
        self.beef_pizza_lbl = tk.Label(master, text="Beef Pizza ($8.99)")
        self.beef_pizza_ent = tk.Entry(master)
        self.chicken_pizza_lbl = tk.Label(master, text="Chicken Pizza ($8.99)")
        self.chicken_pizza_ent = tk.Entry(master)
        self.pork_pizza_lbl = tk.Label(master, text="Pork Pizza ($8.99)")
        self.pork_pizza_ent = tk.Entry(master)
        self.beef_hotdog_lbl = tk.Label(master, text="Beef Hot Dog ($1.99)")
        self.beef_hotdog_ent = tk.Entry(master)
        self.pork_hotdog_lbl = tk.Label(master, text="Pork Hot Dog ($1.99)")
        self.pork_hotdog_ent = tk.Entry(master)
        self.turkey_hotdog_lbl = tk.Label(master, text="Turkey Hot Dog ($1.99)")
        self.turkey_hotdog_ent = tk.Entry(master)

        # Create order button
        self.order_btn = tk.Button(master, text="Place Order", command=self.calculate_total)

        # Create exit button
        self.exit_btn = tk.Button(master, text="Exit", command=master.quit)

        # Pack labels, entry boxes and buttons to the form
        self.beef_pizza_lbl.pack()
        self.beef_pizza_ent.pack()
        self.chicken_pizza_lbl.pack()
        self.chicken_pizza_ent.pack()
        self.pork_pizza_lbl.pack()
        self.pork_pizza_ent.pack()
        self.beef_hotdog_lbl.pack()
        self.beef_hotdog_ent.pack()
        self.pork_hotdog_lbl.pack()
        self.pork_hotdog_ent.pack()
        self.turkey_hotdog_lbl.pack()
        self.turkey_hotdog_ent.pack()
        self.order_btn.pack()
        self.exit_btn.pack()

    def calculate_total(self):
        try:
            # Get input values and calculate total price
            beef_pizza = int(self.beef_pizza_ent.get())
            chicken_pizza = int(self.chicken_pizza_ent.get())
            pork_pizza = int(self.pork_pizza_ent.get())
            beef_hotdog = int(self.beef_hotdog_ent.get())
            pork_hotdog = int(self.pork_hotdog_ent.get())
            turkey_hotdog = int(self.turkey_hotdog_ent.get())

            total_price = (beef_pizza + chicken_pizza + pork_pizza) * 8.99 + \
                          (beef_hotdog + pork_hotdog + turkey_hotdog) * 1.99
            total_price *= 1.07 # Add 7% sales tax

            # Display total price in a message box
            messagebox.showinfo("Total Price", f"Your total bill is ${total_price:.2f}")
        except ValueError:
            # Display error message if input is invalid
            messagebox.showerror("Invalid Input", "Please enter a valid integer for each item.")

# Create main window
root = tk.Tk()

# Create pizza order form
order_form = PizzaOrder(root)

# Run main loop
root.mainloop()