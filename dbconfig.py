import mysql.connector
from mysql.connector import Error

connection = mysql.connector.connect(host='localhost',
									 user='root',
									 password='')

cur = connection.cursor()
cur.execute('CREATE DATABASE adil')
connection.commit()

product_table = 'CREATE TABLE `products` ( `sno` int PRIMARY KEY AUTO_INCREMENT,' \
				' `pid` VARCHAR(50), `pname` VARCHAR(100), `pro_cat` VARCHAR(100),' \
				' `unit_price` int, `qty` int, `location` VARCHAR(255))'

bills_table = 'CREATE TABLE `bills` ( `sno` int PRIMARY KEY AUTO_INCREMENT, `date` VARCHAR(100), `time` VARCHAR(100), `billno` VARCHAR(100))'

category_table = 'CREATE TABLE `category` ( `sno` int PRIMARY KEY AUTO_INCREMENT, `cat_id` VARCHAR(100), `cat_name` VARCHAR(100), `profit` int)'

sales_report_table = 'CREATE TABLE `salesreport` ( `sno` int PRIMARY KEY AUTO_INCREMENT, `date` VARCHAR(100),' \
					 ' `time` VARCHAR(100), `pid` VARCHAR(50), `pro_cat` VARCHAR(100),  `unit_price` int, `qty` int, `profit` int)'


queries = [product_table, bills_table, category_table, sales_report_table]

try:
	connection = mysql.connector.connect(host='localhost',
										 database='adil',
										 user='root',
										 password='')

	cur = connection.cursor()
	for query in queries:
		print(query)
		cur.execute(query)
		connection.commit()
	connection.close()

except Error as e:
	print('connection failed', e)
