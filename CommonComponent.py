# Standard Library Imports
import tkinter as tk
from tkinter import ttk

# User Defined Imports
import DBQuery as db

# Create View Table
def createTable(masterWindow, row, column, data, columnNames):
    # Create Table Title
    j = 0
    for key, value in columnNames.items():
        print(key, value)
        label = tk.Label(master=masterWindow, text=value.get("label"), font=("Calibri", 15, "bold"), bg="white")
        label.grid(row=0, column=j)
        j+=1
    for i in range(row):
        for j in range(column):
            label = tk.Label(master=masterWindow, text=data[i][j], font=("Calibri", 15), bg="white")
            label.grid(row=i+1, column=j)

# Create Insert Form
def createInsertForm(masterWindow, tableName, formData):
    insertFormWindow = tk.Toplevel(master=masterWindow, width=1000, height=700, bg="white")
    insertFormWindow.title("Insert Form")
    entryList = []
    i = 0
    for data in formData:
        label = tk.Label(master=insertFormWindow, text=data.get("name"), font=("Calibri", 15), bg="white", width=15)
        label.grid(row=i, column=0)
        entry = tk.Entry(master=insertFormWindow, font=("Calibri", 15), bg="white", width=15)
        entry.grid(row=i, column=1)
        entryList.append(entry)
        i += 1

    # Back Button
    backBtn = tk.Button(master=insertFormWindow, text="Back", font=("Calibri", 20), bg="cyan", bd=1, width=15, command=insertFormWindow.destroy)
    backBtn.place(x=50, y=550)

    # Submit Button
    submitBtn = tk.Button(master=insertFormWindow, text="Submit", font=("Calibri", 20), bg="cyan", bd=1, width=15, command=lambda: insertAction(insertFormWindow, tableName, entryList))
    submitBtn.place(x=350, y=550)

def insertAction(window, tableName, entries):
    values = []
    for value in entries:
        values.append(value.get())
    db.InsertIntoTable(tableName, values)
    window.destroy()

# Create Update Form
def createUpdateForm(masterWindow, table):
    # print(tableSchema)

    updateFormWindow = tk.Toplevel(master=masterWindow, width=1000, height=700, bg="white")
    updateFormWindow.title("Update Form")
    
    updatableColumnOption = []
    schema = table.get("schema")
    for column in schema:
        updatableColumnOption.append(schema.get(column).get("label"))

    # ID Label
    idLabel = tk.Label(master=updateFormWindow, text="Please Enter ID to update", font=("Calibri", 15), bg="white", width=25)
    idLabel.grid(row=0, column=0)

    # ID Entry
    idEntry = tk.Entry(master=updateFormWindow, font=("Calibri", 15), bg="white", width=15)
    idEntry.grid(row=0, column=1)

    # Column Label
    columnLabel = tk.Label(master=updateFormWindow, text="Please Select Column to update", font=("Calibri", 15), bg="white", width=25)
    columnLabel.grid(row=1, column=0)

    # Column Option Menu
    comboBox = ttk.Combobox(master=updateFormWindow, values=updatableColumnOption, font=("Calibri", 15), width=15)
    comboBox.grid(row=1, column=1)

    # Value Label
    valueLabel = tk.Label(master=updateFormWindow, text="Please Enter New Value", font=("Calibri", 15), bg="white", width=25)
    valueLabel.grid(row=2, column=0)

    # Value Entry
    valueEntry = tk.Entry(master=updateFormWindow, font=("Calibri", 15), bg="white", width=15)
    valueEntry.grid(row=2, column=1)

    # Back Button
    backBtn = tk.Button(master=updateFormWindow, text="Back", font=("Calibri", 20), bg="cyan", bd=1, width=15, command=updateFormWindow.destroy)
    backBtn.grid(row=3, column=0)

    columnToUpdate = None
    for k,v in schema.items():
        if v.get("label") == comboBox.get():
            print(v.get("label"), comboBox.get())
            columnToUpdate = k
            break
    # Submit Button
    submitBtn = tk.Button(master=updateFormWindow, text="Submit", font=("Calibri", 20), bg="cyan", bd=1, width=15, command=lambda: updateAction(updateFormWindow, table, idEntry.get(), comboBox.get(), valueEntry.get()))
    submitBtn.grid(row=3, column=1)

def updateAction(window, table, id, column, value):
    print("Update ID: ",id)
    print("Update Column: ",column)
    print("Update Value: ",value)
    db.UpdateTable(table, id, column, value)
    window.destroy()