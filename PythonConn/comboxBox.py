import tkinter as tk
import mysql.connector
from tkinter import ttk

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = ""
)

mycursor = mydb.cursor()

dbs = []
tables = []
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    for i in x:
        dbs.append(i)

global show
def showTables(dbName):
    mycursor.execute(f"SHOW TABLES IN {dbName}")
    tables.clear()
    for tb in mycursor:
        for tbl in tb:
            tables.append(tbl)
            

    for t in tables:
        lbl = tk.Label(root, text=t)
        lbl.pack(pady=5)

# Function to handle the selection event
def on_select(event):
    selected_value = combo.get()
    showTables(selected_value)

root = tk.Tk()
root.title("Combobox Example")
root.geometry("300x600")

label = tk.Label(root, text="Select an option:")
label.pack(pady=10)

# Creating a combobox
combo = ttk.Combobox(root, values=dbs)
combo.pack(pady=10)

# Binding the selection event to the function
combo.bind("<<ComboboxSelected>>", on_select)

# Setting a default value
combo.current(0)

root.mainloop()
