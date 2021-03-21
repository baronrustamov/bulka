import pymysql.cursors

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
    sql = "SELECT * FROM `wp_posts` WHERE `post_type` IN ('product')"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)