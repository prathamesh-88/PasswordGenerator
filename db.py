import sqlite3

con=sqlite3.connect('username.db')

c=con.cursor()

def entry(acc,un,pw):
	c.execute("INSERT INTO pwd (account,username,password) VALUES (?,?,?)",(acc,un,pw))
	con.commit()
	con.close()

def display():
	c.execute("SELECT * FROM pwd ")
	data=c.fetchall()
	read=""
	for i in data:
		read=read+ i[0]+"   "+i[1]+"   "+i[2]+"\n"
	return data


# c.execute("""CREATE TABLE pwd(
# 			account text,
# 			username text,
# 			password text
# 			)""")

# c.execute("INSERT INTO pwd VALUES ('Orkut','xyz','ojvd*1')")
# c.execute("SELECT * FROM pwd ")
# print(c.fetchall())
# con.commit()
# con.close()

