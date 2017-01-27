import psycopg2
import json

class Json_post():

    @staticmethod
    def load_json_to_postgres():

        try:
            conn=psycopg2.connect(database="E2DS_Madhukar", user="postgres", password="postgres", host="127.0.0.1", port="5432")
            print ("Opened database successfully")
            cur = conn.cursor()
            cur.execute('''CREATE TABLE COMPANY_me4
                   (ID INT PRIMARY KEY     NOT NULL,
                   NAME           TEXT    NOT NULL,
                   AGE            INT     NOT NULL,
                   ADDRESS        CHAR(50),
                   SALARY         REAL);''')

            with open("madhujson.json") as file:
                    data=json.load(file)
                    print(data)
                    print("done here")
                    for dict in data:
                        cur.execute("INSERT INTO COMPANY_me4 (ID,NAME,AGE,ADDRESS,SALARY) VALUES('%s','%s','%s','%s','%s')" % (dict['ID'],dict['NAME'],dict['AGE'],dict['ADDRESS'],dict['SALARY']));
                        print("done upto execute")
                        conn.commit()
                        print("done commit")
                        #conn.close()
            print("dshjdbjbsdj enedededddedd")
        except:
            print("Database insert error")





Json_post.load_json_to_postgres()
# SQL = ("INSERT INTO COMPANY_me3 (ID,NAME,AGE,ADDRESS,SALARY) VALUES ('%d','%s','%d','%s','%d')" % (
# dic['ID'], dic['NAME'], dic['AGE'], dic['ADDRESS'], dic['SALARY']));
# cur.execute("INSERT INTO COMPANY_me3 (ID,NAME,AGE,ADDRESS,SALARY) VALUES({ID},{NAME},{AGE},{ADDRESS},{SALARY})".format(
#     ID=dict['ID'], NAME=dict['NAME'], AGE=dict['AGE'], ADDRESS=dict['ADDRESS'], SALARY=dict['SALARY']));



