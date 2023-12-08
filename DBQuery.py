import oracledb

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

def UpdateTable(tablename, *conditions):
    try:
        cur = con.cursor()
        query = "update " + tablename + " set "
        for i in range(len(conditions)):
            if i == len(conditions) - 1:
                query += conditions[i]
            else:
                query += conditions[i] + ", "
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

# Test Query
# cur = con.cursor()
# data = cur.execute(r"select * from teststudent")
# for row in data:
#     print(row)

# cur.close()
# data = SelectFromTable("ANIMAL")
# for row in data:
#     print(row)


