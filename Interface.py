# Turtleback Zoo GUI Application

# Standard Library Imports
import tkinter as tk

# User Defined Imports
import DBQuery as db
import DBModel as model
import CommonComponent as cmp;


# Asset Management Page
# Asset Management Functions
def openAssetOperationWindow(masterWindow, table, mode):
    assetOperationWindow = tk.Toplevel(master=masterWindow, width=1000, height=700, bg="white")
    assetOperationWindow.title("Asset Management")
    if(mode == 0): # view mode

        data = db.SelectFromTable(table.get("name"))

        if(len(data) == 0):
            print("No data found")
        else:
            column = len(data[0])
            row = len(data)
            # for row in data:
            #     print(row)

            cmp.createTable(assetOperationWindow, row, column, data)
        
        # Back Button
        backBtn = tk.Button(master=assetOperationWindow, text="Back", font=("Calibri", 20), bg="cyan", bd=1, width=15, command=assetOperationWindow.destroy)
        backBtn.place(x=50, y=550)
    
    elif(mode == 1): # insert mode
        cmp.createForm(assetOperationWindow, table)


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

    testBtn = tk.Button(master=tableListWindow, text="Test Student", font=("Calibri", 20), bg="cyan", bd=1, width=15, command=lambda: openAssetOperationWindow(tableListWindow, model.testStudent, mode))
    testBtn.place(x=350, y=400)

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
def openDailyActivity():
    dailyActivityWindow = tk.Toplevel(master=window, width=1000, height=700, bg="white")
    dailyActivityWindow.title("Daily Activity")

    # Daily Activity Page Title
    dailyActivityTitle = tk.Label(master=dailyActivityWindow, text="Daily Activity", font=("Calibri", 50), bg="white", width=25)
    dailyActivityTitle.place(x=50, y=20)

    # Daily Activity Page Buttons
    

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

