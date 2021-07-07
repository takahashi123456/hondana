import sqlite3

#それぞれの変数に入れてあげるとsqlに挿入される
def SQLInsert(titleName,publisherName,AuthorName,Price,ISBN): 

	connect = sqlite3.connect('./db3.sqlite3') 

	cur = connect.cursor()
	
	sql = 'INSERT INTO book ( title, publisher, author, price, ISBN, date) VALUES (?,?,?,?,?, CURRENT_TIMESTAMP);'

	#sql = 'INSERT INTO book ( title, author, ISBN, date) VALUES (?,?,?, CURRENT_TIMESTAMP);'

	insertData = [titleName,publisherName,AuthorName,Price,ISBN]

	cur.execute(sql,insertData)
	connect.commit()
	connect.close()



SQLInsert("testName","testPub","testAuthor",111,12345)
