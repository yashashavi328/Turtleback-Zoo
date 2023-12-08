# Standard Library Imports
import tkinter as tk

# User Defined Imports
import DBQuery as db


def createTable(masterWindow, row, column, data):
    for i in range(row):
        for j in range(column):
            label = tk.Label(master=masterWindow, text=data[i][j], font=("Calibri", 15), bg="white", width=15)
            label.grid(row=i, column=j)

def createForm(masterWindow, table):
    # print(tableSchema)

    insertFormWindow = tk.Toplevel(master=masterWindow, width=1000, height=700, bg="white")
    insertFormWindow.title("Insert Form")
    entryList = []
    tableSchema = table.get("schema")
    i = 0
    for schema in tableSchema:
        label = tk.Label(master=insertFormWindow, text=tableSchema.get(schema).get("label"), font=("Calibri", 15), bg="white", width=15)
        label.grid(row=i, column=0)
        entry = tk.Entry(master=insertFormWindow, font=("Calibri", 15), bg="white", width=15)
        entry.grid(row=i, column=1)
        entryList.append(entry)
        i += 1

    # Back Button
    backBtn = tk.Button(master=insertFormWindow, text="Back", font=("Calibri", 20), bg="cyan", bd=1, width=15, command=insertFormWindow.destroy)
    backBtn.place(x=50, y=550)

    # Submit Button
    submitBtn = tk.Button(master=insertFormWindow, text="Submit", font=("Calibri", 20), bg="cyan", bd=1, width=15, command=lambda: insertAction(insertFormWindow, table.get("name"), entryList))
    submitBtn.place(x=350, y=550)

def insertAction(window, tableName, entries):
    values = []
    for value in entries:
        values.append(value.get())
    db.InsertIntoTable(tableName, values)
    window.destroy()