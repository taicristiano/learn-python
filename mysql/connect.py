import pymysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='csdltai1234',
                             db='pymysql'
                            )
print(connection)
#connection = pymysql.connect(host_name, username, host_password, port, database_name)

try:
    with connection.cursor() as cursor:
        # create a database
        #query = "CREATE DATABASE pymysql"
        # print(cursor.execute(query)) # Output: 1
        # query = """
        #     CREATE TABLE `person` (
        #         `id` int(11) NOT NULL AUTO_INCREMENT,
        #         `email` varchar(255) NOT NULL,
        #         `password` varchar(255) NOT NULL,
        #         PRIMARY KEY (`id`)
        #     ) ENGINE=InnoDB DEFAULT CHARSET=utf8
        #     AUTO_INCREMENT=1
        # """
        # cursor.execute(query)

        # insert
        # sql = "INSERT INTO `person` (`email`, `password`) VALUES (%s, %s)"
        # cursor.execute(sql, ('admin@toidicode.com', '123456'))

        # # commit
        # connection.commit()

        # get data
        sql = "SELECT * FROM person"
        resultCount = cursor.execute(sql)

        # print('Data Count: ' + resultCount.len())

        print(cursor.fetchone())

finally:
    # close connection
    connection.close()
    # https://toidicode.com/get-data-mysql-qua-python-401.html