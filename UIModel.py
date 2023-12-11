# test data

testStudent = {
    "name": "teststudent",
    "schema":{
        "NAME": {"type": "str", "label": "Name", "isEditable": True},
        "GENDER": {"type": "str", "label": "Gender", "isEditable": True},
        "EMAIL": {"type": "str", "label": "Email", "isEditable": True},
    },
    "primaryKey": "NAME"
}

# actual data
dailyReport = {
    "name": "Daily Report",
    "schema":{
        "NAME": {"type": "str", "label": "Name"},
        "TYPE": {"type": "str", "label": "Type"},
        "REVENUE": {"type": "float", "label": "Revenue"},
        "TICKETS_SOLD": {"type": "float", "label": "Tickets Sold"},
    },
}

animalPopulation = {
    "name": "Animal Population",
    "schema":{
        "SNAME": {"type": "str", "label": "Species Name"},
        "STATUS": {"type": "str", "label": "Health Status"},
        "POPULATION": {"type": "float", "label": "Population"},
    },
}

speciesMonthlyCost = {
    "name": "Species Monthly Cost",
    "schema":{
        "SNAME": {"type": "str", "label": "Species Name"},
        "MONTHLY_FOOD_COST": {"type": "float", "label": "Monthly Food Cost"},
        "VCOST": {"type": "float", "label": "Veterinarian Cost"},
        "SCOST": {"type": "float", "label": "Specialist Cost"},
    },
}

topThree = {
    "name": "Top Attractions",
    "schema":{
        "NAME": {"type": "str", "label": "Name"},
        "REVENUE": {"type": "float", "label": "Revenue"},
    },
}

best5Days = {
    "name": "Peak Revenue Days",
    "schema":{
        "DATE": {"type": "datetime", "label": "Date"},
        "REVENUE": {"type": "float", "label": "Revenue"},
    },
}

avgRevenue = {
    "name": "Average Revenue",
    "schema":{
        "NAME": {"type": "str", "label": "Name"},
        "TYPE": {"type": "str", "label": "Type"},
        "AVG_REVENUE": {"type": "float", "label": "Revenue"},
    },
}