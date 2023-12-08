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

employee = {}


