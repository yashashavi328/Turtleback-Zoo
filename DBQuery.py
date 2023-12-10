import oracledb
import datetime

con = oracledb.connect(dsn='turtlebackzoodb', user='yp328', password='SuperSecret@007', sid='course', config_dir=r"C:\oracle\instantclient_21_12\network\admin")
print("Connected to Oracle DB successfully")
# con.close()

# Insert Query
def InsertIntoTable(tablename, values):
    try:
        cur = con.cursor()
        query = "insert into " + tablename + " values ("
        for i in range(len(values)):
            if i == len(values) - 1:
                query += "'{0}'".format(values[i]) + ")"
            else:
                query += "'{0}'".format(values[i]) + ", "
        print(query)
        cur.execute(query) # execute the query
        con.commit() # commit the changes
        print("Insertion Successful")
    except Exception as e:
        print("Insertion Failed")
        print(e)
    finally:
        cur.close()

def DeleteFromTable(tablename, *conditions):
    try:
        cur = con.cursor()
        query = "delete from " + tablename + " where "
        for i in range(len(conditions)):
            if i == len(conditions) - 1:
                query += conditions[i]
            else:
                query += conditions[i] + " and "
        print(query)
        cur.execute(query) # execute the query
        con.commit() # commit the changes
        print("Deletion Successful")
    except Exception as e:
        print("Deletion Failed")
        print(e)
    finally:
        cur.close()

def UpdateTable(table, id, column, value):
    try:
        cur = con.cursor()
        query = "update {0} set {1}='{2}' where {3}='{4}'".format(table.get("name"), column, value, table.get("primaryKey"), id)   
        print(query)
        cur.execute(query) # execute the query
        con.commit() # commit the changes
        print("Update Successful")
    except Exception as e:
        print("Update Failed")
        print(e)
    finally:
        cur.close()

def SelectFromTable(tablename, *conditions):
    try:
        cur = con.cursor()
        query = "select * from " + tablename
        print(query)
        if len(conditions) == 0:
            print(query)
            cur.execute(query) # execute the query
            data = cur.fetchall() # fetch all the data
            print("Selection Successful")
            return data
        else:
            query += " where "
            for i in range(len(conditions)):
                if i == len(conditions) - 1:
                    query += conditions[i]
                else:
                    query += conditions[i] + " and "
            print(query)
            cur.execute(query) # execute the query
            data = cur.fetchall()
            print("Selection Successful")
            return data
    except Exception as e:
        print("Selection Failed")
        print(e)
    finally:
        cur.close()

# Zoo Activity
def AddActivityEvent(values):
    try:
        print(values)
        cur = con.cursor()
        date = datetime.datetime.now().strftime("%d-%b-%y")
        print(date)
        entry = SelectFromTable("revenue_events", "revenue_id={0}".format(values[0]),"event_date='{0}'".format(date))
        print("entry",entry)
        if entry is not None and len(entry) > 0:
            revenue = entry[0][2]+values[1]
            ticketSold = entry[0][3]+values[2]
            query = "update revenue_events set revenue={0}, ticket_sold={1} where revenue_id={2} and event_date='{3}'".format(revenue, ticketSold, values[0], date)
        else:
            query = "insert into revenue_events values ({0}, '{1}', {2}, {3})".format(values[0], date, values[1], values[2])
        print("query: ", query)
        cur.execute(query) # execute the query
        con.commit() # commit the changes
        print("Insertion Successful")
    except Exception as e:
        print("Add activity Failed")
        print(e)
    finally:
        cur.close()

# Reporting & Management
def getReportByDate(date):
    try:
        cur = con.cursor()
        query = "select * from revenue_events where event_date='{0}'".format(date)
        print(query)
        cur.execute(query) # execute the query
        data = cur.fetchall() # fetch all the data
        print("Selection Successful")
        return data
    except Exception as e:
        print("Selection Failed")
        print(e)
    finally:
        cur.close()

def getAnimalPopulationReport():
    pass

def getTopThreeAttractionShow(beginDate, endDate):
    try:
        cur = con.cursor()
        query = """select name, total_revenue
                from (select re.revenue_id, rt.name as name, total_revenue, dense_rank() over (order by total_revenue desc) as ranking
                from revenue_type rt, (select revenue_id, sum(revenue) as total_revenue 
                from revenue_events 
                where event_date between '{0}' and '{1}'
                group by revenue_id
                order by total_revenue desc) re
                where rt.revenue_id=re.revenue_id
                and rt.type='attraction show')
                where ranking<=3;""".format(beginDate, endDate)
        print(query)
        cur.execute(query) # execute the query
        data = cur.fetchall() # fetch all the data
        print("Selection Successful")
        return data
    except Exception as e:
        print("Selection Failed")
        print(e)
    finally:
        cur.close()

def getFiveBestDaysByMonth(month):
    try:
        cur = con.cursor()
        query = """select * from (select event_date, sum(revenue) as total_revenue 
                from revenue_events 
                where event_date like '%-{0}-%'
                group by event_date
                order by total_revenue desc)
                where rownum<=5;""".format(month)
        print(query)
        cur.execute(query) # execute the query
        data = cur.fetchall() # fetch all the data
        print("Selection Successful")
        return data
    except Exception as e:
        print("Selection Failed")
        print(e)
    finally:
        cur.close()

def getAverageRevenue(beginDate, endDate):
    try:
        cur = con.cursor()
        query = """select rt.name, rt.type, re.avg_revenue
                from revenue_type rt,
                (select revenue_id, avg(revenue) as avg_revenue
                from revenue_events
                where event_date between '{0}' and '{1}'
                group by revenue_id) re
                where rt.revenue_id = re.revenue_id
                order by rt.type;""".format(beginDate, endDate)
        print(query)
        cur.execute(query) # execute the query
        data = cur.fetchall() # fetch all the data
        print("Selection Successful")
        return data
    except Exception as e:
        print("Selection Failed")
        print(e)
    finally:
        cur.close()
# Test Query
# cur = con.cursor()
# data = cur.execute(r"select * from teststudent")
# for row in data:
#     print(row)

# cur.close()
# data = SelectFromTable("ANIMAL")
# for row in data:
#     print(row)


