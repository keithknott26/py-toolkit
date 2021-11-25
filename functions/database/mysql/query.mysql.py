###############################################################
#
#                  DATABASE FUNCTIONS
#
###############################################################

import mysql.connector

def select_query(host, user, password, database, sql, mode):
    rows = []
    # mode = single to fetch one row
    # mode = multi to fetch all rows
    # Connect to server
    config = {
        'host' : host,
        'port' : 3306,
        'user' : user,
        'password' : password,
        'database' : database,
        'charset': 'utf8',
        'use_unicode': False,
        'connection_timeout': 3
    }
    
    #Connect to Database
    try:
        db = mysql.connector.Connect(**config)
        
        # Get a cursor
        cursor = db.cursor()
        # Execute a query
        cursor.execute(sql)
    
        if mode == "single":
            # Fetch one result
            row = cursor.fetchone()
            rows.append(row[0])
        elif mode == "multi":
            #Returns object with multiple rows
            for row in cursor.fetchall():
                rows.append(row)
        else:
            if debug:
                print(debugStr, "select_query(): Mode was not specified correctly")
            # Close connection
            cursor.close()
            db.close()
    except:
        if debug:
            print(debugStr, "select_query(): Could not connect or query failed on host: " + host)
    
    return rows
    
def query_dwhglobal(host, alertid):
    # CCS Voice DB Config
    user = report_db_username
    password = report_db_password
    database = "global"
    mode = "single"
    
    sql = 'select ClusterID from tblAlert INNER JOIN tblCluster where fkCluster_ID=pkCluster_ID AND AlertId="' + alertid + '"'
    row=select_query(host, user, password, database, sql, mode)
    if debug:
        print(debugStr, "Database Query Result: " + str(row) + " (host: " + host + ")")
    
    if len(row) > 0 and row != None:
        output = row[0]
        return output, host
    else:
        return None, None
        #output = []
    
