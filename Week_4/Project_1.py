import tkinter as tk
import pandas as pd
df = pd.read_csv('GIG-logistics.csv')
root = tk.Tk()
root.title("Employee Verification")

# Create label and entry for name
name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

# Create label and entry for department
department_label = tk.Label(root, text="Department:")
department_label.pack()
department_entry = tk.Entry(root)
department_entry.pack()

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=lambda: verify_employee(name_entry.get(), department_entry.get()))
submit_button.pack()

# Create a display area for the result
result_label = tk.Label(root, text="")
result_label.pack()
def verify_employee(name, department):
    # Check if the employee exists in the dataset
    if name in df['Name'].values and department in df['Department'].values:
        # Get the other members of the department
        department_members = df.loc[(df['Name'] != name) & (df['Department'] == department), 'Name'].tolist()
        result = f"Welcome, {name}! Other members of your department are: {', '.join(department_members)}"
    else:
        result = f"Employee '{name}' from the '{department}' department does not exist."
    result_label.config(text=result)
root.mainloop()

