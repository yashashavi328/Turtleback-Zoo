# Turtleback Zoo GUI Application

# Standard Library Imports
import tkinter as tk

# User Defined Imports
import DBQuery as db
import DBModel as model
import CommonComponent as cmp
from Constant import *


# Asset Management Page
# Asset Management Functions
def openAssetOperationWindow(masterWindow, tableData, mode):
    # assetOperationWindow = tk.Toplevel(master=masterWindow, bg="white")
    # assetOperationWindow.title("Asset Management")
    data = db.SelectFromTable(tableData.get("name"))
    if(mode == 0): # view mode
        if(len(data) == 0):
            print("No data found")
        else:
            column = len(data[0])
            row = len(data)
            cmp.createTable(masterWindow, row, column, data, tableData.get("schema"))
    
    elif(mode == 1): # insert mode
        formData = []
        for column, columnMetadata in tableData.get("schema").items():
            print(column, columnMetadata)
            if(columnMetadata.get("isEditable")):
                formData.append({
                    "name": columnMetadata.get("label"),
                    "type": columnMetadata.get("type")
                })
        cmp.createInsertForm(masterWindow, tableData.get("name"), formData)

    # elif(mode == 2): # update mode
    #     cmp.createUpdateForm(masterWindow, table)

def openTableListWindow(masterWindow, mode):
    tableListWindow = tk.Toplevel(master=masterWindow, width=1000, height=700, bg="white")
    tableListWindow.title("Asset Management")

    # Asset Management Page Title
    tableListTitle = tk.Label(master=tableListWindow, text="Assets", font=("Calibri", 50), bg="white", width=25)
    tableListTitle.place(x=50, y=20)

    # Asset Management Page Buttons
    assetBtn = tk.Button(master=tableListWindow, text="Species", font=("Calibri", 20), bg="cyan", bd=1, width=15, command=lambda: openAssetOperationWindow(tableListWindow, model.species, mode))
    assetBtn.place(x=50, y=250)

    animalBtn = tk.Button(master=tableListWindow, text="Animal", font=("Calibri", 20), bg="cyan", bd=1, width=15, command=lambda: openAssetOperationWindow(tableListWindow, model.animal, mode))
    animalBtn.place(x=350, y=250)

    employeeBtn = tk.Button(master=tableListWindow, text="Employee", font=("Calibri", 20), bg="cyan", bd=1, width=15, command=lambda: openAssetOperationWindow(tableListWindow, model.employee, mode))
    employeeBtn.place(x=650, y=250)

    buildingBtn = tk.Button(master=tableListWindow, text="Building", font=("Calibri", 20), bg="cyan", bd=1, width=15, command=lambda: openAssetOperationWindow(tableListWindow, model.building, mode))
    buildingBtn.place(x=50, y=400)

    revenueBtn = tk.Button(master=tableListWindow, text="Revenue Type", font=("Calibri", 20), bg="cyan", bd=1, width=15, command=lambda: openAssetOperationWindow(tableListWindow, model.revenueType, mode))
    revenueBtn.place(x=350, y=400)

    testBtn = tk.Button(master=tableListWindow, text="Test Student", font=("Calibri", 20), bg="cyan", bd=1, width=15, command=lambda: openAssetOperationWindow(tableListWindow, model.testStudent, mode))
    testBtn.place(x=650, y=400)


    # Back Button
    backBtn = tk.Button(master=tableListWindow, text="Back", font=("Calibri", 20), bg="cyan", bd=1, width=15, command=tableListWindow.destroy)
    backBtn.place(x=50, y=550)

def openAssetMgmt():
    mode = {
        "view": 0,
        "insert": 1,
        "update": 2
    }

    # assetMgmt = tk.Frame(master=window, width=baseWidth, height=baseHeight, bg="white")
    assetMgmtWindow = tk.Toplevel(master=window, width=1000, height=700, bg="white")
    assetMgmtWindow.title("Asset Management")

    # Asset Management Page Title
    assetMgmtTitle = tk.Label(master=assetMgmtWindow, text="Asset Management", font=("Calibri", 50), bg="white", width=25)
    assetMgmtTitle.place(x=50, y=20)

    # Asset Management Page Buttons
    viewBtn = tk.Button(master=assetMgmtWindow, text="View Asset", font=("Calibri", 20), bg="cyan", bd=1, width=15, command=lambda: openTableListWindow(assetMgmtWindow, mode["view"]))
    viewBtn.place(x=50, y=250)

    insertBtn = tk.Button(master=assetMgmtWindow, text="Insert Asset", font=("Calibri", 20), bg="cyan", bd=1, width=15, command=lambda: openTableListWindow(assetMgmtWindow, mode["insert"]))
    insertBtn.place(x=350, y=250)

    updateBtn = tk.Button(master=assetMgmtWindow, text="Update Asset", font=("Calibri", 20), bg="cyan", bd=1, width=15, command=lambda: openTableListWindow(assetMgmtWindow, mode["update"]))
    updateBtn.place(x=650, y=250)

# Daily Activity Page
def openActivityWindow(masterWindow, revenueType, mode):
    if(mode == 0): # view mode
        condition = "type = '{0}'".format(revenueType)
        data = db.SelectFromTable("revenue_type", condition)
        if(len(data) == 0):
            print("No data found")
        else:
            column = len(data[0])
            row = len(data)
            cmp.createTable(masterWindow, row, column, data, model.revenueType.get("schema"))
    elif(mode == 1):
        formData = []
        condition = "type = '{0}'".format(revenueType)
        data = db.SelectFromTable("revenue_type", condition)
        

        activityInsertFormWindow = tk.Toplevel(master=masterWindow, width=1000, height=700, bg="white")
        activityInsertFormWindow.title("Insert Form")

        if(revenueType == "attraction show"):
            # Activity Label
            activityLabel = tk.Label(master=activityInsertFormWindow, text="Please Select Activity", font=("Calibri", 15), bg="white", width=25)
            activityLabel.grid(row=0, column=0)

            activityOption = []
            for row in data:
                activityOption.append(row[1])
            
            activityVar = tk.StringVar(activityInsertFormWindow)
            activityVar.set(activityOption[0])
            activityMenu = tk.OptionMenu(activityInsertFormWindow, activityVar, *activityOption)
            activityMenu.grid(row=0, column=1)

            # Customer Type Label
            customerTypeLabel = tk.Label(master=activityInsertFormWindow, text="Please Select Customer Type", font=("Calibri", 15), bg="white", width=25)
            customerTypeLabel.grid(row=1, column=0)

            customerTypeOption = []
            for key, value in CustomerType.items():
                customerTypeOption.append(value.get("name"))
            
            customerTypeVar = tk.StringVar(activityInsertFormWindow)
            customerTypeVar.set(customerTypeOption[0])
            customerTypeMenu = tk.OptionMenu(activityInsertFormWindow, customerTypeVar, *customerTypeOption)
            customerTypeMenu.grid(row=1, column=1)

            # Quantity Label
            quantityLabel = tk.Label(master=activityInsertFormWindow, text="Please Enter Quantity", font=("Calibri", 15), bg="white", width=25)
            quantityLabel.grid(row=2, column=0)
            quantityEntry = tk.Entry(master=activityInsertFormWindow, font=("Calibri", 15), bg="white", width=25)
            quantityEntry.grid(row=2, column=1)

            # Back Button
            backBtn = tk.Button(master=activityInsertFormWindow, text="Back", font=("Calibri", 20), bg="cyan", bd=1, width=15, command=activityInsertFormWindow.destroy)
            backBtn.grid(row=3, column=0)

            def submit():    
                activityId = None
                ticketPrice = None
                for row in data:
                    if(row[1] == activityVar.get()):
                        print("row", row)
                        activityId = row[0]
                        if(customerTypeVar.get() == "Adult"):
                            ticketPrice = row[4]
                        elif(customerTypeVar.get() == "Senior"):
                            ticketPrice = row[5]
                        elif(customerTypeVar.get() == "Children"):
                            ticketPrice = row[6]
                        break
                print(activityId, ticketPrice)
                db.AddActivityEvent([activityId, ticketPrice*int(quantityEntry.get()), int(quantityEntry.get())])
            # Submit Button
            submitBtn = tk.Button(master=activityInsertFormWindow, text="Submit", font=("Calibri", 20), bg="cyan", bd=1, width=15, command=submit)
            submitBtn.grid(row=3, column=1)

        elif(revenueType == "concession"):
            #Activity Label
            activityLabel = tk.Label(master=activityInsertFormWindow, text="Please Select Product", font=("Calibri", 15), bg="white", width=25)
            activityLabel.grid(row=0, column=0)

            activityOption = []
            for row in data:
                activityOption.append(row[7])
            
            activityVar = tk.StringVar(activityInsertFormWindow)
            activityVar.set(activityOption[0])
            activityMenu = tk.OptionMenu(activityInsertFormWindow, activityVar, *activityOption)
            activityMenu.grid(row=0, column=1)

            # Quantity Label
            quantityLabel = tk.Label(master=activityInsertFormWindow, text="Please Enter Quantity", font=("Calibri", 15), bg="white", width=25)
            quantityLabel.grid(row=1, column=0)
            quantityEntry = tk.Entry(master=activityInsertFormWindow, font=("Calibri", 15), bg="white", width=25)
            quantityEntry.grid(row=1, column=1)

            # Back Button
            backBtn = tk.Button(master=activityInsertFormWindow, text="Back", font=("Calibri", 20), bg="cyan", bd=1, width=15, command=activityInsertFormWindow.destroy)
            backBtn.grid(row=2, column=0)

            def submit():    
                activityId = None
                productPrice = None
                for row in data:
                    if(row[7] == activityVar.get()):
                        print("row", row)
                        activityId = row[0]
                        productPrice = row[8]
                        break
                print(activityId, productPrice)
                db.AddActivityEvent([activityId, productPrice*int(quantityEntry.get()), int(quantityEntry.get())])
            # Submit Button
            submitBtn = tk.Button(master=activityInsertFormWindow, text="Submit", font=("Calibri", 20), bg="cyan", bd=1, width=15, command=submit)
            submitBtn.grid(row=2, column=1)

        elif(revenueType == "admission"):
            #Activity Label
            activityLabel = tk.Label(master=activityInsertFormWindow, text="Please Select Ticket Type", font=("Calibri", 15), bg="white", width=25)
            activityLabel.grid(row=0, column=0)

            activityOption = []
            for row in data:
                activityOption.append(row[1])
            
            ticketVar = tk.StringVar(activityInsertFormWindow)
            ticketVar.set(activityOption[0])
            ticketMenu = tk.OptionMenu(activityInsertFormWindow, ticketVar, *activityOption)
            ticketMenu.grid(row=0, column=1)

             # Customer Type Label
            customerTypeLabel = tk.Label(master=activityInsertFormWindow, text="Please Select Customer Type", font=("Calibri", 15), bg="white", width=25)
            customerTypeLabel.grid(row=1, column=0)

            customerTypeOption = []
            for value in CustomerType.values():
                customerTypeOption.append(value.get("name"))
            
            customerTypeVar = tk.StringVar(activityInsertFormWindow)
            customerTypeVar.set(customerTypeOption[0])
            customerTypeMenu = tk.OptionMenu(activityInsertFormWindow, customerTypeVar, *customerTypeOption)
            customerTypeMenu.grid(row=1, column=1)

            # Quantity Label
            quantityLabel = tk.Label(master=activityInsertFormWindow, text="Please Enter Quantity", font=("Calibri", 15), bg="white", width=25)
            quantityLabel.grid(row=2, column=0)
            quantityEntry = tk.Entry(master=activityInsertFormWindow, font=("Calibri", 15), bg="white", width=25)
            quantityEntry.grid(row=2, column=1)

            # Back Button
            backBtn = tk.Button(master=activityInsertFormWindow, text="Back", font=("Calibri", 20), bg="cyan", bd=1, width=15, command=activityInsertFormWindow.destroy)
            backBtn.grid(row=3, column=0)

            def submit():    
                activityId = None
                ticketPrice = None
                for row in data:
                    if(row[1] == ticketVar.get()):
                        print("row", row)
                        activityId = row[0]
                        if(customerTypeVar.get() == "Adult"):
                            ticketPrice = row[4]
                        elif(customerTypeVar.get() == "Senior"):
                            ticketPrice = row[5]
                        elif(customerTypeVar.get() == "Children"):
                            ticketPrice = row[6]
                        break
                print(activityId, ticketPrice)
                db.AddActivityEvent([activityId, ticketPrice*int(quantityEntry.get()), int(quantityEntry.get())])
            # Submit Button
            submitBtn = tk.Button(master=activityInsertFormWindow, text="Submit", font=("Calibri", 20), bg="cyan", bd=1, width=15, command=submit)
            submitBtn.grid(row=3, column=1)

def openActivityListWindow(masterWindow, mode):
    activityListWindow = tk.Toplevel(master=masterWindow, width=1000, height=700, bg="white")
    activityListWindow.title("Daily Activity")

    # Asset Management Page Title
    activityListTitle = tk.Label(master=activityListWindow, text="Activities", font=("Calibri", 50), bg="white", width=25)
    activityListTitle.place(x=50, y=20)

    # Asset Management Page Buttons
    attractionShowBtn = tk.Button(master=activityListWindow, text="Attraction Show", font=("Calibri", 20), bg="cyan", bd=1, width=15, command=lambda: openActivityWindow(activityListWindow, "attraction show", mode))
    attractionShowBtn.place(x=50, y=250)

    concessionBtn = tk.Button(master=activityListWindow, text="Concession", font=("Calibri", 20), bg="cyan", bd=1, width=15, command=lambda: openActivityWindow(activityListWindow, "concession", mode))
    concessionBtn.place(x=350, y=250)

    admissionBtn = tk.Button(master=activityListWindow, text="Admission", font=("Calibri", 20), bg="cyan", bd=1, width=15, command=lambda: openActivityWindow(activityListWindow, "admission", mode))
    admissionBtn.place(x=650, y=250)

    # Back Button
    backBtn = tk.Button(master=activityListWindow, text="Back", font=("Calibri", 20), bg="cyan", bd=1, width=15, command=activityListWindow.destroy)
    backBtn.place(x=50, y=550)

def openDailyActivity():
    mode = {
        "view": 0,
        "insert": 1,
    }


    dailyActivityWindow = tk.Toplevel(master=window, width=1000, height=700, bg="white")
    dailyActivityWindow.title("Daily Activity")

    # Daily Activity Page Title
    dailyActivityTitle = tk.Label(master=dailyActivityWindow, text="Daily Activity", font=("Calibri", 50), bg="white", width=25)
    dailyActivityTitle.place(x=50, y=20)

    # Daily Activity Page Buttons
    viewBtn = tk.Button(master=dailyActivityWindow, text="View Activity", font=("Calibri", 20), bg="cyan", bd=1, width=15, command=lambda: openActivityListWindow(dailyActivityWindow, mode["view"]))
    viewBtn.place(x=150, y=250)

    insertBtn = tk.Button(master=dailyActivityWindow, text="Add Activity", font=("Calibri", 20), bg="cyan", bd=1, width=15, command=lambda: openActivityListWindow(dailyActivityWindow, mode["insert"]))
    insertBtn.place(x=450, y=250)
    
# Reporting Page
def openReporting():
    reportingWindow = tk.Toplevel(master=window, width=1000, height=700, bg="white")
    reportingWindow.title("Management & Reporting")

    # Daily Activity Page Title
    reportingTitle = tk.Label(master=reportingWindow, text="Management & Reporting", font=("Calibri", 50), bg="white", width=25)
    reportingTitle.place(x=50, y=20)


# Home Page
window = tk.Tk()
window.title("Turtleback Zoo")
window.geometry("1200x800")

baseHeight = 800
baseWidth = 1200
home = tk.Frame(master=window, width=baseWidth, height=baseHeight, bg="white")
home.pack(fill=tk.BOTH, expand=True)

# Home Page Title
homeTitle = tk.Label(master=home, text="TURTLEBACK ZOO", font=("Calibri", 50), bg="white")
homeTitle.place(x=350, y=50)

# Home Page Buttons
assetMgmtBtn = tk.Button(master=home, text="Asset Management", font=("Calibri", 20), bg="white", bd=3, width=50, command=openAssetMgmt)
assetMgmtBtn.place(x=250, y=200)

dailyActivityBtn = tk.Button(master=home, text="Daily Activity", font=("Calibri", 20), bg="white", bd=3, width=50, command=openDailyActivity)
dailyActivityBtn.place(x=250, y=350)

reportingBtn = tk.Button(master=home, text="Management & Reporting", font=("Calibri", 20), bg="white", bd=3, width=50, command=openReporting)
reportingBtn.place(x=250, y=500)

window.mainloop()

