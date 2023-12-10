# Database table models

# test data

testStudent = {
    "name": "TESTSTUDENT",
    "schema":{
        "NAME": {"type": "str", "label": "Name"},
        "GENDER": {"type": "str", "label": "Gender"},
        "EMAIL": {"type": "str", "label": "Email"}
    }
}

# actual data
animal = {
    "name": "ANIMAL",
    "schema": {
        "ANIMAL_ID": {"type":"float", "label": "Animal ID"},
        "STATUS": {"type":"str", "label": "Status"},
        "BIRTH_YEAR": {"type":"float", "label": "Birth Year"},
        "CAGE_ID": {"type": "float", "label": "Cage ID"},
        "SPECIES_ID": {"type": "float", "label": "Species ID"},
    },
    "primarykey": "ANIMAL_ID"
}

species = {
    "name": "SPECIES",
    "schema": {
        "SPECIES_ID": {"type": "float", "label": "Species ID"},
        "NAME": {"type":"str", "label": "Name"},
        "DIET": {"type":"str", "label": "Diet"},
        "POPULATION": {"type": "float", "label": "Population"},
        "MONTHLY_FOOD_COST": {"type": "float", "label": "Monthly Food Cost"},
        "VETERINARIAN_ID": {"type": "float", "label": "Veterinarian ID"},
        "SPECIALIST_TRAINER_ID": {"type": "float", "label": "Specialist Trainer ID"}
    },
    "primarykey": "SPECIES_ID"
}

building = {
    "name": "BUILDING",
    "schema": {
        "BUILDING_ID": {"type": "float", "label": "Building ID"},
        "NAME": {"type": "str", "label": "Building Name"},
        "SQ_FEET": {"type": "float", "label": "Area(sq feet)"},
        "NUM_FLOORS": {"type": "float", "label": "Number of Floors"},
    },
    "primarykey": "BUILDING_ID"
}

cage = {
    "name": "CAGE",
    "schema": {
        "CAGE_ID": {"type": "float", "label": "Cage ID"},
        "SQ_FEET": {"type": "float", "label": "Area(sq feet)"},
        "BUILDING_ID": {"type": "float", "label": "Building ID"},
    },
    "primarykey": "CAGE_ID"
}

revenueType = {
    "name": "REVENUE_TYPE",
    "schema": {
        "REVENUE_ID": {"type": "float", "label": "Revenue ID"},
        "TYPE": {"type": "str", "label": "Revenue Type"},
        "NAME": {"type": "str", "label": "Name"},
        "BUILDING_ID": {"type": "float", "label": "Building ID"},
    },
    "primarykey": "REVENUE_ID"
}

revenueEvent = {
    "name": "REVENUE_EVENT",
    "schema": {
        "REVENUE_ID": "float",
        "EVENT_DATE": "datetime",
        "REVENUE": "float",
        "TICKET_SOLD": "float"
    },
    "primarykey": "REVENUE_ID"
}

attractionShow = {
    "name": "ATTRACTION_SHOW",
    "schema": {
        "REVENUE_ID": {"type": "float", "label": "Revenue ID"},
        "SHOWS_PER_DAY": {"type": "float", "label": "Shows Per Day"},
        "ADULT_TICKET_PRICE": {"type": "float", "label": "Adult Ticket Price"},
        "CHILDREN_TICKET_PRICE": {"type": "float", "label": "Children Ticket Price"},
        "SENIOR_TICKET_PRICE": {"type": "float", "label": "Senior Ticket Price"},
    },
    "primarykey": "REVENUE_ID"
}

concession = {
    "name": "CONCESSION",
    "schema": {
        "REVENUE_ID": {"type": "float", "label": "Revenue ID"},
        "PRODUCT": {"type": "str", "label": "Product"},
    },
    "primarykey": "REVENUE_ID"
}

admission = {
    "name": "ADMISSION",
    "schema": {
        "REVENUE_ID": {"type": "float", "label": "Revenue ID"},
        "ADULT_TICKET_PRICE": {"type": "float", "label": "Adult Ticket Price"},
        "CHILDREN_TICKET_PRICE": {"type": "float", "label": "Children Ticket Price"},
        "SENIOR_TICKET_PRICE": {"type": "float", "label": "Senior Ticket Price"},
    },
    "primarykey": "REVENUE_ID"
}

employee = {
    "name": "EMPLOYEE",
    "schema": {
        "EMPLOYEE_ID": {"type": "float", "label": "Employee ID"},
        "LAST_NAME" :{"type": "str", "label": "Last Name"},
        "START_DATE" :{"type": "datetime", "label": "Start Date"},
        "APARTMENT":{"type": "str", "label": "Apartment"},
        "STREET" :{"type": "str", "label": "Street"},
        "STATE" :{"type": "str", "label": "State"},
        "ZIPCODE" :{"type": "str", "label": "Zip Code"},
        "PHONE_NUM" :{"type": "str", "label": "Phone Number"},
        "JOB_TYPE" :{"type": "str", "label": "Job Type"},
        "SUPERVISOR_ID" :{"type": "float", "label": "Supervisor ID"},
        "FLAG_VETERINARIAN" :{"type": "str", "label": "Flag Veterinarian"},
        "LICENSE_NUM" :{"type": "str", "label": "License Number"},
        "DEGREE_YR" :{"type": "float", "label": "Degree Year"},
        "FLAG_ANIMAL_CARE_TRAINER" :{"type": "str", "label": "Flag Animal Care Trainer"},
        "FLAG_MAINTENANCE" :{"type": "str", "label": "Flag Maintenance"},
        "FLAG_CUSTOMER_SERVICE" :{"type": "str", "label": "Flag Customer Service"},
        "FLAG_TICKET_SELLER" :{"type": "str", "label": "Flag Ticket Seller"},
    },
    "primarykey": "EMPLOYEE_ID"
}

hourlyRate = {
    "name": "HOURLY_RATE",
    "schema": {
        "HID": {"type": "float", "label": "Hourly ID"},
        "JOB_TYPE": {"type": "str", "label": "Job Type"},
        "PAY": {"type": "float", "label": "Hourly Rate"},
    },
    "primarykey": "HID"
}

participatesIn = {
    "name": "PARTICIPATES_IN",
    "schema": {
        "ANIMAL_ID": {"type": "float", "label": "Animal ID"},
        "REVENUE_ID": {"type": "float", "label": "Revenue ID"},
    },
    "primarykey": "REVENUE_ID"
}
