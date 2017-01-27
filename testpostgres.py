import psycopg2
conn=psycopg2.connect(database="E2DS_Madhukar", user="postgres", password="postgres", host="127.0.0.1", port="5432")
print ("Opened database successfully")
cur = conn.cursor()
cur.execute("insert into MADDY (id,name,age,address,salary) values (24,'madhu21',2321,'Austin21',1222221);")
conn.commit()
print("Insertion done")
conn.close()


# import json
#
# with open("madhujson.json") as f:
#     data = json.load(f)
# print(data)
#
# print(data[0]['id'])


x = 2
print("%s" %(x))