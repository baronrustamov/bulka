import pymysql.cursors
import json

# Connect to the database
connection = pymysql.connect(host='54.189.52.114',
                             user='ubuntu',
                             password='ubuntu',
                             database='wordpress',
                             cursorclass=pymysql.cursors.DictCursor)

#with connection:
    #with connection.cursor() as cursor:
        # Create a new record
     #   sql = "INSERT INTO `customers` (`email`, `password`) VALUES (%s, %s)"
      #  cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    #connection.commit()

with connection.cursor() as cursor:
    # Read a single record
    sql = "SELECT `post_title`, `post_excerpt` FROM `wp_posts` WHERE `post_type` IN ('product')"
    cursor.execute(sql)
    print(cursor.description)
    result = cursor.fetchall()
    print(result)
    res1 = json.JSONEncoder().encode(result)
    print(res1)
    res2 = json.loads(res1)
    print(res2)
    #res3 = res2[0]["post_title"] + ':\n' + res2[0]["post_excerpt"]
    for i in range(1):
        print(res2[i]["post_title"] + ':\n' + res2[i]["post_excerpt"])
    #print(res3)
    #dbinfo = pymysql.Connection.close(connection)
    #out = result[0]
    #print(out)
    print(pymysql.get_client_info())
cursor.close()
connection.close()