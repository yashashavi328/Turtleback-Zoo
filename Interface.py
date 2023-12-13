# Turtleback Zoo GUI Application
# Standard Library Imports
import tkinter as tk
import datetime as dt
from tkcalendar import Calendar

# User Defined Imports
import DBQuery as db
import DBModel as model
import UIModel as uiModel
import CommonComponent as cmp
from Constant import *

# Asset Management Page
def openAssetOperationWindow(masterWindow, tableData, mode):
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
    animalBtn = tk.Button(master=tableListWindow, text="Animal", font=("Calibri", 20), bg="cyan", bd=1, width=15, command=lambda: openAssetOperationWindow(tableListWindow, model.animal, mode))
    animalBtn.place(x=50, y=250)

    buildingBtn = tk.Button(master=tableListWindow, text="Building", font=("Calibri", 20), bg="cyan", bd=1, width=15, command=lambda: openAssetOperationWindow(tableListWindow, model.building, mode))
    buildingBtn.place(x=350, y=250)

    revenueBtn = tk.Button(master=tableListWindow, text="Attraction", font=("Calibri", 20), bg="cyan", bd=1, width=15, command=lambda: openAssetOperationWindow(tableListWindow, model.revenueType, mode))
    revenueBtn.place(x=650, y=250)

    employeeBtn = tk.Button(master=tableListWindow, text="Employee", font=("Calibri", 20), bg="cyan", bd=1, width=15, command=lambda: openAssetOperationWindow(tableListWindow, model.employee, mode))
    employeeBtn.place(x=50, y=400)

    assetBtn = tk.Button(master=tableListWindow, text="Hourly Wage", font=("Calibri", 20), bg="cyan", bd=1, width=15, command=lambda: openAssetOperationWindow(tableListWindow, model.hourlyRate, mode))
    assetBtn.place(x=350, y=400)

    # Back Button
    backBtn = tk.Button(master=tableListWindow, text="Back", font=("Calibri", 20), bg="yellow", bd=1, width=15, command=tableListWindow.destroy)
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
            backBtn = tk.Button(master=activityInsertFormWindow, text="Back", font=("Calibri", 20), bg="yellow", bd=1, width=15, command=activityInsertFormWindow.destroy)
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
            submitBtn = tk.Button(master=activityInsertFormWindow, text="Submit", font=("Calibri", 20), bg="green2", bd=1, width=15, command=submit)
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
            backBtn = tk.Button(master=activityInsertFormWindow, text="Back", font=("Calibri", 20), bg="yellow", bd=1, width=15, command=activityInsertFormWindow.destroy)
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
            submitBtn = tk.Button(master=activityInsertFormWindow, text="Submit", font=("Calibri", 20), bg="green2", bd=1, width=15, command=submit)
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
            backBtn = tk.Button(master=activityInsertFormWindow, text="Back", font=("Calibri", 20), bg="yellow", bd=1, width=15, command=activityInsertFormWindow.destroy)
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
            submitBtn = tk.Button(master=activityInsertFormWindow, text="Submit", font=("Calibri", 20), bg="green2", bd=1, width=15, command=submit)
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
    backBtn = tk.Button(master=activityListWindow, text="Back", font=("Calibri", 20), bg="yellow", bd=1, width=15, command=activityListWindow.destroy)
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
def openAnimalReportWindow(masterWindow, reportType):
    if(reportType == 1):
        data = db.getAnimalPopulationReport()
        if(data is None or len(data) == 0):
            print("No data found")
        else:
            column = len(data[0])
            row = len(data)
            cmp.createTable(masterWindow, row, column, data, uiModel.animalPopulation.get("schema"))
    elif(reportType == 2):
        data = db.getSpeciesMonthlyCostReport()
        if(data is None or len(data) == 0):
            print("No data found")
        else:
            column = len(data[0])
            row = len(data)
            cmp.createTable(masterWindow, row, column, data, uiModel.speciesMonthlyCost.get("schema"))

def openReportingWindow(masterWindow, reportType):
    # Reporting 
    if(reportType == 1):
        # Report By Date
        reportByDateWindow = tk.Toplevel(master=masterWindow, width=1000, height=700, bg="white")
        reportByDateWindow.title("Report & Management")

        # Report By Date Page Title
        top3AttTitle = tk.Label(master=reportByDateWindow, text="Report By Date", font=("Calibri", 50), bg="white", width=25)
        top3AttTitle.place(x=50, y=20)

        # Date Label
        dateLabel = tk.Label(master=reportByDateWindow, text="Please Select Date", font=("Calibri", 15), bg="white", width=25)
        dateLabel.place(x=50, y=250)

        # Date Entry
        currentDate = dt.datetime.now()
        dateEntry = Calendar(reportByDateWindow, selectmode="day", year=currentDate.year, month=currentDate.month, day=currentDate.day, date_pattern="mm/dd/yy")
        dateEntry.place(x=350, y=250, )

        # Back Button
        backBtn = tk.Button(master=reportByDateWindow, text="Back", font=("Calibri", 20), bg="yellow", bd=1, width=15, command=reportByDateWindow.destroy)
        backBtn.place(x=50, y=550)

        def submit():
            data = db.getReportByDate(dateEntry.get_date())
            print(data)
            if(data is None or len(data) == 0):
                print("No data found")
            else:
                column = len(data[0])
                row = len(data)
                cmp.createTable(masterWindow, row, column, data, uiModel.dailyReport.get("schema"))
                reportByDateWindow.destroy()

        # Submit Button
        submitBtn = tk.Button(master=reportByDateWindow, text="Submit", font=("Calibri", 20), bg="green2", bd=1, width=15, command=submit)
        submitBtn.place(x=350, y=550)
    elif(reportType == 2):
        # Report By Date
        reportByDateWindow = tk.Toplevel(master=masterWindow, width=1000, height=700, bg="white")
        reportByDateWindow.title("Report & Management")

        # Report By Date Page Title
        top3AttTitle = tk.Label(master=reportByDateWindow, text="Animal Population & Cost", font=("Calibri", 50), bg="white", width=25)
        top3AttTitle.place(x=50, y=20)

        populationBtn = tk.Button(master=reportByDateWindow, text="Animal Population", font=("Calibri", 15), bg="cyan", bd=3, width=25, command=lambda: openAnimalReportWindow(reportByDateWindow, 1))
        populationBtn.place(x=150, y=250)

        monthlyCostBtn = tk.Button(master=reportByDateWindow, text="Monthly Cost", font=("Calibri", 15), bg="cyan", bd=3, width=25, command=lambda: openAnimalReportWindow(reportByDateWindow, 2))
        monthlyCostBtn.place(x=500, y=250)

    elif(reportType == 3):
        # Report By Date
        reportByDateWindow = tk.Toplevel(master=masterWindow, width=1000, height=700, bg="white")
        reportByDateWindow.title("Report & Management")

        # Report By Date Page Title
        reportByDateTitle = tk.Label(master=reportByDateWindow, text="Top 3 Attraction", font=("Calibri", 50), bg="white", width=25)
        reportByDateTitle.place(x=50, y=20)

        currentDate = dt.datetime.now()
        
        # Date Label
        dateLabel = tk.Label(master=reportByDateWindow, text="Please Select Beginning Date", font=("Calibri", 15), bg="white", width=25)
        dateLabel.place(x=50, y=150)

        # Date Entry
        beginDate = Calendar(reportByDateWindow, selectmode="day", year=currentDate.year, month=currentDate.month, day=currentDate.day, date_pattern="mm/dd/yy")
        beginDate.place(x=350, y=150, )

         # Date Label
        dateLabel = tk.Label(master=reportByDateWindow, text="Please Select Ending Date", font=("Calibri", 15), bg="white", width=25)
        dateLabel.place(x=50, y=350)

        # Date Entry
        endDate = Calendar(reportByDateWindow, selectmode="day", year=currentDate.year, month=currentDate.month, day=currentDate.day, date_pattern="mm/dd/yy")
        endDate.place(x=350, y=350, )

        # Back Button
        backBtn = tk.Button(master=reportByDateWindow, text="Back", font=("Calibri", 20), bg="yellow", bd=1, width=15, command=reportByDateWindow.destroy)
        backBtn.place(x=50, y=550)

        def submit():
            data = db.getTopThreeAttractionShow(beginDate.get_date(), endDate.get_date())
            print(data)
            if(data is None or len(data) == 0):
                print("No data found")
            else:
                column = len(data[0])
                row = len(data)
                cmp.createTable(masterWindow, row, column, data, uiModel.topThree.get("schema"))
                reportByDateWindow.destroy()
        # Submit Button
        submitBtn = tk.Button(master=reportByDateWindow, text="Submit", font=("Calibri", 20), bg="green2", bd=1, width=15, command=submit)
        submitBtn.place(x=350, y=550)
    elif(reportType == 4):
        # Report By Date
        reportByDateWindow = tk.Toplevel(master=masterWindow, height=400, width=620, bg="white")
        reportByDateWindow.title("Report & Management")

        # Report By Date Page Title
        reportByDateTitle = tk.Label(master=reportByDateWindow, text="Best 5 days of Month", font=("Calibri", 50), bg="white")
        reportByDateTitle.place(x=20, y=20)

        # Month Selection
        monthLabel = tk.Label(master=reportByDateWindow, text="Please Select a Month", font=("Calibri", 15), bg="white", width=25)
        monthLabel.place(x=50, y=120)
        
        monthOption = []
        for row in Month.values():
            monthOption.append(row.get("name"))
        
        monthVar = tk.StringVar(reportByDateWindow)
        monthVar.set(monthOption[0])
        monthMenu = tk.OptionMenu(reportByDateWindow, monthVar, *monthOption)
        monthMenu.place(x=350, y=120)

         # Back Button
        backBtn = tk.Button(master=reportByDateWindow, text="Back", font=("Calibri", 20), bg="yellow", bd=1, width=15, command=reportByDateWindow.destroy)
        backBtn.place(x=50, y=250)

        def submit():
            monthVal = None
            for value in Month.values():
                if(value.get("name") == monthVar.get()):
                    monthVal = value.get("query")
                    break
            data = db.getFiveBestDaysByMonth(monthVal)
            print(data)
            if(data is None or len(data) == 0):
                print("No data found")
            else:
                tableData = []
                for row in data:
                    row = list(row)
                    row[0] = row[0].strftime("%d-%b-%y")
                    tableData.append(row)
                column = len(tableData[0])
                row = len(tableData)
                cmp.createTable(masterWindow, row, column, tableData, uiModel.best5Days.get("schema"))
                reportByDateWindow.destroy()
        # Submit Button
        submitBtn = tk.Button(master=reportByDateWindow, text="Submit", font=("Calibri", 20), bg="green2", bd=1, width=15, command=submit)
        submitBtn.place(x=300, y=250)
    elif(reportType == 5):
         # Report By Date
        reportByDateWindow = tk.Toplevel(master=masterWindow, width=1000, height=700, bg="white")
        reportByDateWindow.title("Report & Management")

        # Report By Date Page Title
        reportByDateTitle = tk.Label(master=reportByDateWindow, text="Average Revenue in a Duration", font=("Calibri", 50), bg="white", width=25)
        reportByDateTitle.place(x=50, y=20)

        currentDate = dt.datetime.now()
        
        # Date Label
        dateLabel = tk.Label(master=reportByDateWindow, text="Please Select Beginning Date", font=("Calibri", 15), bg="white", width=25)
        dateLabel.place(x=50, y=150)

        # Date Entry
        beginDate = Calendar(reportByDateWindow, selectmode="day", year=currentDate.year, month=currentDate.month, day=currentDate.day, date_pattern="mm/dd/yy")
        beginDate.place(x=350, y=150, )

         # Date Label
        dateLabel = tk.Label(master=reportByDateWindow, text="Please Select Ending Date", font=("Calibri", 15), bg="white", width=25)
        dateLabel.place(x=50, y=350)

        # Date Entry
        endDate = Calendar(reportByDateWindow, selectmode="day", year=currentDate.year, month=currentDate.month, day=currentDate.day, date_pattern="mm/dd/yy")
        endDate.place(x=350, y=350, )

        # Back Button
        backBtn = tk.Button(master=reportByDateWindow, text="Back", font=("Calibri", 20), bg="yellow", bd=1, width=15, command=reportByDateWindow.destroy)
        backBtn.place(x=50, y=550)

        def submit():
            data = db.getAverageRevenue(beginDate.get_date(), endDate.get_date())
            print(data)
            if(data is None or len(data) == 0):
                print("No data found")
            else:
                column = len(data[0])
                row = len(data)
                cmp.createTable(masterWindow, row, column, data, uiModel.avgRevenue.get("schema"))
                reportByDateWindow.destroy()
        # Submit Button
        submitBtn = tk.Button(master=reportByDateWindow, text="Submit", font=("Calibri", 20), bg="green2", bd=1, width=15, command=submit)
        submitBtn.place(x=350, y=550)

def openReporting():
    reportingWindow = tk.Toplevel(master=window, width=1000, height=700, bg="white")
    reportingWindow.title("Management & Reporting")

    # Daily Activity Page Title
    reportingTitle = tk.Label(master=reportingWindow, text="Management & Reporting", font=("Calibri", 50), bg="white", width=25)
    reportingTitle.place(x=50, y=20)
    
    # Daily Activity Page Buttons
    btn1 = tk.Button(master=reportingWindow, text="Report by Date", font=("Calibri", 20), bg="cyan", bd=1, width=15, command=lambda: openReportingWindow(reportingWindow, 1))
    btn1.place(x=150, y=250)

    btn2 = tk.Button(master=reportingWindow, text="Animal Report", font=("Calibri", 20), bg="cyan", bd=1, width=15, command=lambda: openReportingWindow(reportingWindow, 2))
    btn2.place(x=450, y=250)

    btn3 = tk.Button(master=reportingWindow, text="Top 3 Attraction", font=("Calibri", 20), bg="cyan", bd=1, width=15, command=lambda: openReportingWindow(reportingWindow, 3))
    btn3.place(x=750, y=250)

    btn4 = tk.Button(master=reportingWindow, text="Top 5 Days of Month", font=("Calibri", 20), bg="cyan", bd=1, width=20, command=lambda: openReportingWindow(reportingWindow, 4))
    btn4.place(x=250, y=400)

    btn5 = tk.Button(master=reportingWindow, text="Average Revenue", font=("Calibri", 20), bg="cyan", bd=1, width=20, command=lambda: openReportingWindow(reportingWindow, 5))
    btn5.place(x=600, y=400)


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

