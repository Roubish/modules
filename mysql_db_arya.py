#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 14:16:30 2022

@author: dragon
"""

import mysql.connector as connector

def connection():
    try:
        c = connector.connect(
        	host='arya-prod.cubaxiuycgsa.ap-south-1.rds.amazonaws.com',
            user="hb",
            password='assertarya123',
            port=3306,
            database='arya_db'
        )
        return c
    except:
        print("connection error")
        exit(1)


def test1(): #no error method
    cn = connection()
    cur = cn.cursor()
    cur.execute("TRUNCATE TABLE data_camera_new;")
    print(cur.fetchone())
test1()


#%%
## CONNECT DATA ONLY
import mysql.connector

mydb = mysql.connector.connect(
	host='arya-prod.cubaxiuycgsa.ap-south-1.rds.amazonaws.com',
    user="hb",
    password='assertarya123',
    port=3306,
    database='arya_db'
)

print(mydb)
## CONNECT DATA ONLY

#%%
mycursor = mydb.cursor()

mycursor.execute("SELECT warehouse_id,camera_id, camera_name FROM data_camera;")

myresult = mycursor.fetchall()


data_camera = []
for i in range(len(myresult)):
    channel = myresult[i][1].split('_')[1]
    if myresult[i][2]!='null' and myresult[i][2]!='null ':
        if int(channel)<8:
            data_camera.append(myresult[i])


#%%
mycursor = mydb.cursor()

mycursor.execute("SELECT warehouse_id,rtsp_link,camera_company FROM data_warehouse;")

data_warehouse = mycursor.fetchall()

final_data = []
for k in range(len(data_warehouse)):
    ip = data_warehouse[k][1].split('@')[2].split('/')[0].split(':')[0]
    port = data_warehouse[k][1].split('@')[2].split('/')[0].split(':')[1]
    wh_id = data_warehouse[k][0]
    for i in range(len(data_camera)):
        if data_warehouse[k][0]==data_camera[i][0]:
            channel = data_camera[i][1].split('_')[1]
# =============================================================================
#             if data_warehouse[k][0]<50:
#                 channel = channel
#             else:
#                 if channel=='4':
#                     channel = '2'
#                 if channel=='5':
#                     channel = '3'
#                 if channel=='7':
#                     channel = '4'
# =============================================================================
            temp=(data_camera[i][1],data_camera[i][0],data_camera[i][2],'admin','assert@123',port,ip,channel,data_warehouse[k][2])
            final_data.append(temp)



#%%

## PUSH DATA
## PUSH DATA
print('Database Pushing Started..........')

mycursor = mydb.cursor()
sql = "INSERT INTO data_camera_new (camera_id, warehouse_id, name, username, password, port, ip, channel, munufacturer)\
VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s)"
mycursor.executemany(sql, final_data)
mydb.commit()


print('Database Updated..........')
# =============================================================================
# #%%
# columns = "camera_id, warehouse_id, name, username, password, port, ip, channel, munufacturer"
# query = "TRUNCATE TABLE data_camera_new;"
# mycursor.execute(query)
# mydb.commit()
# 
# mycursor.execute("CREATE TABLE data_camera_new (id INT AUTO_INCREMENT PRIMARY KEY, camera_id VARCHAR(255),  warehouse_id VARCHAR(255),name VARCHAR(255),username VARCHAR(255),password VARCHAR(255),port VARCHAR(255),ip VARCHAR(255),channel VARCHAR(255),munufacturer VARCHAR(255))")
# 
# #%%
# 
# import pandas as pd
# df = pd.read_sql("select * from data_camera", mydb)
# print(df.columns)
# 
# 
# 
# #%% 
# 
mydb.close()
# =============================================================================
