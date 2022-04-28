import pymysql

conn = pymysql.connect(host='54.180.79.115',
                       port=52146,
                       user='admin',
                       password='123qwe',
                       db='csweb',
                       charset='utf8')




sql = "INSERT INTO Customer (CustomerID, CustomerName, ContactName, Address, City, PostalCode, Country, id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)";

with conn:
    with conn.cursor() as cur:
        for i in range(0,59):
            cur.execute(sql, ('CustomerID-'+str(i), 'Number-'+str(i), 'ContactName-'+str(i), str(110)+str(i),'city-'+str(i),str(i),'Country-'+str(i),str(i)));
        conn.commit()