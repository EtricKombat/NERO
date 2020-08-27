# with open('infrastructure-diagram.jpeg','rb') as f:
#     m =f.read()
# with open("recieved.jpeg",'wb') as q:
#     q.write(m)
try:
    import os
    import sys
    import psycopg2 as pg2

except:
    print('not')


def create_database():
#     # print(name)
#     # print(image)
        try:

            conn = pg2.connect(database="allripe", user="postgres", password="5mimosa", host="localhost", port="5433")
                # print("working")
        except:
            print("not working")
        curr = conn.cursor()

        # curr.execute(
        # 'INSERT INTO "dronepics"("FILENAME", "BINARYDATA") VALUES (%s, %s)',
        # (name,image))
        frut = "pear"
        query ='select fruitsname FROM fruits where id =1 '

        curr.execute(query )

        rows = curr.fetchall()

        for r in rows:

            result=f"{r[0]}"
        return (result)
        conn.commit()
        curr.close()
        conn.close()

# file_name = []
# for root, dirs, files in os.walk("."):
#     for filename in files:
#         file_name.append(filename)
#
#         with open(filename, 'rb') as f:
#             x =f.read()
#         create_database(filename,x)
# print((file_name))
# for root, dirs, files in os.walk ("."):
#      for filename in files:
#         print(filename)
#         with open(os.path.join(root,filename), 'rb') as f:
#             x =f.read()
create_database()
        # print(os.path.join(root,filename))
