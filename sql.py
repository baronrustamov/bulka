import pymysql.cursors
import json



# Connect to the database
connection = pymysql.connect(host='54.189.52.114',
                             user='ubuntu',
                             password='zyrzak-kizfa4-nAcdog',
                             database='mainbulka',
                             cursorclass=pymysql.cursors.DictCursor)

#with connection:
    #with connection.cursor() as cursor:
        # Create a new record
     #   sql = "INSERT INTO `customers` (`email`, `password`) VALUES (%s, %s)"
      #  cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    #connection.commit()
'''
with connection.cursor() as cursor:
    # Read a single record
    sql = "SELECT * FROM `products` WHERE 1"
    cursor.execute(sql)
    print(cursor.description)
    result = cursor.fetchall()
    print(result)
    count = cursor.rowcount
    print(count)
    i = 0
    while i < count:
        print(result[i])
        i = i + 1
    i = 0
    while i < count:
        print(result[i]["productName"])
        i = i + 1
    for row in cursor:
        print(row)
cursor.close()
connection.close()
'''


with connection.cursor() as cursor:
    # Read a single record
    sql = "select * from `subscriptions` inner join `products` on mainbulka.subscriptions.subscproducts = mainbulka.products.productCode inner join customers on mainbulka.subscriptions.customerNumber = mainbulka.customers.customerNumber"
    cursor.execute(sql)
    #print(cursor.description)
    result = cursor.fetchall()
    #print(result)
    count = cursor.rowcount
    print(count)

    i = 0
    #while i < count:
    #    print(result[i])
    #    i = i + 1

    for n < count:
        while result[i]["customerNumber"] == i:
            print(result[i]["subscproducts"])

        i = i+1

   # i = 0
    #while i < count:
    #    print(result[i]["productName"])
    #    i = i + 1

    for row in cursor:
        print(row)
cursor.close()
connection.close()