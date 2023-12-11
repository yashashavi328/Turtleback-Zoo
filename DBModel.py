# Database table models

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
animal = {
    "name": "animal",
    "schema": {
        "ANIMAL_ID": {"type":"float", "label": "Animal ID", "isEditable": True},
        "STATUS": {"type":"str", "label": "Status", "isEditable": True},
        "BIRTH_YEAR": {"type":"float", "label": "Birth Year", "isEditable": True},
        "CAGE_ID": {"type": "float", "label": "Cage ID", "isEditable": True},
        "SPECIES_ID": {"type": "float", "label": "Species ID", "isEditable": True},
        "NAME": {"type": "str", "label": "Name", "isEditable": True},
    },
    "primarykey": "ANIMAL_ID"
}

species = {
    "name": "species",
    "schema": {
        "SPECIES_ID": {"type": "float", "label": "Species ID", "isEditable": True},
        "NAME": {"type":"str", "label": "Name", "isEditable": True},
        "DIET": {"type":"str", "label": "Diet", "isEditable": True},
        "POPULATION": {"type": "float", "label": "Population", "isEditable": True},
        "MONTHLY_FOOD_COST": {"type": "float", "label": "Monthly Food Cost", "isEditable": True},
        "VETERINARIAN_ID": {"type": "float", "label": "Veterinarian ID", "isEditable": True},
        "SPECIALIST_TRAINER_ID": {"type": "float", "label": "Specialist Trainer ID", "isEditable": True}
    },
    "primarykey": "SPECIES_ID"
}

building = {
    "name": "building",
    "schema": {
        "BUILDING_ID": {"type": "float", "label": "Building ID", "isEditable": True},
        "NAME": {"type": "str", "label": "Building Name", "isEditable": True},
        "SQ_FEET": {"type": "float", "label": "Area(sq feet)", "isEditable": True},
        "NUM_FLOORS": {"type": "float", "label": "Number of Floors", "isEditable": True},
    },
    "primarykey": "BUILDING_ID"
}

cage = {
    "name": "cage",
    "schema": {
        "CAGE_ID": {"type": "float", "label": "Cage ID", "isEditable": True},
        "SQ_FEET": {"type": "float", "label": "Area(sq feet)", "isEditable": True},
        "BUILDING_ID": {"type": "float", "label": "Building ID", "isEditable": True},
    },
    "primarykey": "CAGE_ID"
}

revenueType = {
    "name": "revenue_type",
    "schema": {
        "revenue_id": {"type": "float", "label": "Revenue ID", "isEditable": True},
        "name": {"type": "str", "label": "Name", "isEditable": True},
        "type": {"type": "str", "label": "Revenue Type", "isEditable": True},
        "attraction_show_name": {"type": "str", "label": "Show Name", "isEditable": True},
        "adult_ticket_price": {"type": "float", "label": "Ticket Price(Adult)", "isEditable": True},
        "senior_ticket_price": {"type": "float", "label": "Ticket Price(Senior)", "isEditable": True},
        "children_ticket_price": {"type": "float", "label": "TIcket Price(Children)", "isEditable": True},
        "product": {"type": "str", "label": "Product", "isEditable": True},
        "product_price": {"type": "float", "label": "Price", "isEditable": True},
        "building_id": {"type": "float", "label": "Building ID", "isEditable": True},
    },
    "primarykey": "REVENUE_ID"
}

revenueEvent = {
    "name": "revenue_event",
    "schema": {
        "REVENUE_ID": {"type": "float", "label": "Revenue ID", "isEditable": True},
        "EVENT_DATE": {"type": "datetime", "label": "Event Date", "isEditable": True},
        "REVENUE": {"type": "float", "label": "Revenue"}, "isEditable": True,
        "TICKET_SOLD": {"type": "float", "label": "Ticket Sold", "isEditable": True},
    },
    "primarykey": "REVENUE_ID"
}

employee = {
    "name": "EMPLOYEE",
    "schema": {
        "EMPLOYEE_ID": {"type": "float", "label": "Employee ID"},
        "FIRST_NAME": {"type": "str", "label": "First Name"},
        "LAST_NAME": {"type": "str", "label": "Last Name"},
        "START_DATE": {"type": "date", "label": "Start Date"},
        "APARTMENT": {"type": "str", "label": "Apartment"},
        "STREET": {"type": "str", "label": "Street"},
        "STATE": {"type": "str", "label": "State"},
        "ZIPCODE": {"type": "str", "label": "Zipcode"},
        "PHONE_NUM": {"type": "str", "label": "Phone Number"},
        "JOB_TYPE": {"type": "str", "label": "Job Type"},
        "SUPERVISOR_ID": {"type": "float", "label": "Supervisor ID"},
        "FLAG_VETERINARIAN": {"type": "str", "label": "Flag Veterinarian"},
        "LICENSE_NUM": {"type": "str", "label": "License Number"},
        "DEGREE_YR": {"type": "float", "label": "Degree Year"},
        "FLAG_ANIMAL_CARE_TRAINER": {"type": "str", "label": "Flag Animal Care Trainer"},
        "FLAG_MAINTENANCE": {"type": "str", "label": "Flag Maintenance"},
        "FLAG_CUSTOMER_SERVICE": {"type": "str", "label": "Flag Customer Service"},
        "FLAG_TICKET_SELLER": {"type": "str", "label": "Flag Ticket Seller"},
    },
    "primarykey": "EMPLOYEE_ID"
}


