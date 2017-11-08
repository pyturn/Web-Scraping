# This code watch the filesystem (particular folder), list all the files present in the folder, applies queries to that file (queries
# are fixed for each file) and feed it into the database. All the work is dynamic here. And if somehow query do not get executes then it
# will transfer that file to folder named "Success" otherwise folder named "failure".

# Here psycopg2 is used which is Postgresql database adapter for the python programming language.
import psycopg2,pdb,os
#psycopg2.sql contains objects and functions useful to generate SQL dynamically.
from psycopg2 import sql

#Connecting with the database of company,path of the files,folders (where it will transfer after succesful or failure operation). 
conn = psycopg2.connect(database="dwh_20170612", user = "enter_your_id", password = "enter_your_password", host = "127.0.0.1", port = "5555")
path = "/home/localserver/ftp/file"
path1 = "/home/localserver/ftp/success"
path2 = "/home/localserver/ftp/failure"
cur = conn.cursor()

#List all the files and save their name into an array.
files = os.listdir(path)
# "mst_file_action" is the table in database which have the filename,table_name,action_name,compare_key.
cur.execute("SELECT * FROM mst_file_action;")
records = cur.fetchall()
#pdb.set_trace()


def appendi(file_name, table_name, compare_key):
	file = path+"/"+file_name
	file_success = path1 + "/" + file_name
	file_failure = path2 + "/" + file_name
#	pdb.set_trace()
#   Another connection is created for child process.
	conn_tmp = psycopg2.connect(database="dwh_20170612", user = "enter_your_id", password = "enter_your_password", host = "127.0.0.1", port = "5555")
	cur_tmp = conn_tmp.cursor()
	try:
#       Creating temporary table in which the fields are exactly same as database_table.
		cur_tmp.execute(sql.SQL("CREATE TEMP TABLE tmp_t2 (like {} );").format(sql.Identifier(table_name)))
		conn_tmp.commit()
		table_name_1 = 'tmp_t2'
#		Copying the content of file to temporary table. 
		cur_tmp.execute(sql.SQL("COPY {} FROM %s DELIMITER ',' CSV HEADER;").format(sql.Identifier(table_name_1)),(file,))
		conn_tmp.commit()
#       Appending all that data which is not in the database table from temporary table.
		cur_tmp.execute(sql.SQL("INSERT INTO {0} SELECT * FROM {1} WHERE NOT EXISTS (SELECT 1 FROM {0} WHERE {1}.{2}={0}.{2});").format(sql.Identifier(table_name),sql.Identifier(table_name_1),sql.Identifier(compare_key)))
		conn_tmp.commit()
	except Exception as e:
#		If somehow the above process unable to get execute then do the same process again by making another connection. 
		try:
			conn_tmp1 = psycopg2.connect(database="dwh_20170612", user = "enter_your_id", password = "enter_your_password", host = "127.0.0.1", port = "5555")
			cur_tmp1 = conn_tmp1.cursor()
			cur_tmp1.execute(sql.SQL("CREATE TEMP TABLE tmp_t21 (like {} );").format(sql.Identifier(table_name)))
			table_name_1 = 'tmp_t21'
			cur_tmp1.execute(sql.SQL("COPY {} FROM %s DELIMITER ',' CSV HEADER;").format(sql.Identifier(table_name_1)),(file,))
			conn_tmp1.commit()
			cur_tmp1.execute(sql.SQL("INSERT INTO {0} SELECT * FROM {1} WHERE NOT EXISTS (SELECT 1 FROM {0} WHERE {1}.{2}={0}.{2});").format(sql.Identifier(table_name),sql.Identifier(table_name_1),sql.Identifier(compare_key)))
			conn_tmp1.commit()
			conn_tmp1.close()
		except:
#			Moving the file to failure_folder.
			os.rename(file,file_failure)
	conn_tmp.close()	
	



def inserti(file_name, table_name):
	file = path+"/"+file_name
	file_success = path1 + "/" + file_name
	file_failure = path2 + "/" + file_name
#	pdb.set_trace()
#   Another connection is created for child process.
	conn_tmp = psycopg2.connect(database="dwh_20170612", user = "enter_your_id", password = "enter_your_password", host = "127.0.0.1", port = "5555")
	cur_tmp = conn_tmp.cursor()
#   Truncating the table in database to insert the data into it.	
	cur_tmp.execute(sql.SQL("truncate {};").format(sql.Identifier(table_name)))
	conn_tmp.commit()
	try:
#		Copy the file to the table in database.
		cur_tmp.execute(sql.SQL("COPY {} FROM %s DELIMITER ',' CSV HEADER;").format(sql.Identifier(table_name)),(file,))
		conn_tmp.commit()
#		Transferring the file to Success folder.		
		os.rename(file,file_success)
	except Exception as e:
#	Executing the same above process by making different connection.
		try:
			conn_tmp1 = psycopg2.connect(database="dwh_20170612", user = "enter_your_id", password = "enter_your_password", host = "127.0.0.1", port = "5555")
			cur_tmp1 = conn_tmp1.cursor()
			cur_tmp1.execute(sql.SQL("COPY {} FROM %s DELIMITER ',' CSV HEADER;").format(sql.Identifier(table_name)),(file,))
			conn_tmp1.commit()
			os.rename(file,file_success)
			conn_tmp1.close()
		except:
#			If unable to execute the process then transferring the file to failure folder.			
			os.rename(file,file_failure)
	conn_tmp.close()





def updatei(file_name,table_name,compare_key):
	file = path+"/"+file_name
	file_success = path1 + "/" + file_name
	file_failure = path2 + "/" + file_name
#	pdb.set_trace()
#   Creating connection for child process.
	conn_tmp = psycopg2.connect(database="dwh_20170612", user = "enter_your_id", password = "enter_your_password", host = "127.0.0.1", port = "5555")
	cur_tmp = conn_tmp.cursor()
	try:
#		Creating the temporary table exactly same as the permanent table and copyting the file in it.
		cur_tmp.execute(sql.SQL("CREATE TEMP TABLE tmp_t2 (like {} );").format(sql.Identifier(table_name)))
		table_name_1 = 'tmp_t2'
		cur_tmp.execute(sql.SQL("COPY {} FROM %s DELIMITER ',' CSV HEADER;").format(sql.Identifier(table_name_1)),(file,))
		conn_tmp.commit()
		cur_tmp.execute("SELECT * FROM tmp_t2;")
#		List having all the column name present in the table of database excluding the column of compare_key.
		colnames = []
		for desc in cur_tmp.description:
			if desc[0] != str(compare_key):
				colnames.append(desc[0])
#		Executing query separately for each column.
		for i in colnames:
			cur_tmp.execute(sql.SQL('''UPDATE {0}
				SET {1} = tmp_t2.{1}
				FROM tmp_t2
				WHERE {2}.{3} = tmp_t2.{3}
				;''').format(sql.Identifier(table_name),sql.Identifier(i),sql.Identifier(table_name),sql.Identifier(compare_key)))
		conn_tmp.commit()
#		Moving the file to success folder.
		os.rename(file,file_success)
	except:
		try:
#			Executing the same above process by making different connection.
			conn_tmp1 = psycopg2.connect(database="dwh_20170612", user = "enter_your_id", password = "enter_your_password", host = "127.0.0.1", port = "5555")
			cur_tmp1 = conn_tmp1.cursor()
			cur_tmp1.execute(sql.SQL("CREATE TEMP TABLE tmp_t21 (like {} );").format(sql.Identifier(table_name)))
			table_name_1 = 'tmp_t21'
			cur_tmp1.execute(sql.SQL("COPY {} FROM %s DELIMITER ',' CSV HEADER;").format(sql.Identifier(table_name_1)),(file,))
			conn_tmp1.commit()
			cur_tmp1.execute("SELECT * FROM tmp_t21;")
			colnames = []
			for desc in cur_tmp1.description:
				if desc[0] != str(compare_key):
					colnames.append(desc[0])
			for i in colnames:
				cur_tmp1.execute(sql.SQL('''UPDATE {0}
				SET {1} = tmp_t21.{1}
				FROM tmp_t21
				WHERE {2}.{3} = tmp_t21.{3}
				;''').format(sql.Identifier(table_name),sql.Identifier(i),sql.Identifier(table_name),sql.Identifier(compare_key)))
			os.rename(file,file_success)
			conn_tmp1.commit()
			conn_tmp1.close()
		except:
#			Moving the file to failure folder if the process does not execute.
			os.rename(file,file_failure)
	conn_tmp.close()



#Applying a for loop on the file in files and on the basis of filename calling the function to apply action on it, by passing file_name,
#variable_name,table_name,compare_key through variables.
#Whenever update function is called it first append that file to the list and then update it.
for file in files:
	for i in range(len(records)):
		if (records[i][0]==file):
			table_name = records[i][1]
			operation_name = records[i][2]
			compare_key = records[i][3]
			if(operation_name == "INSERT"):
				inserti(records[i][0],table_name)
			elif(operation_name == "UPDATE"):
				appendi(records[i][0], table_name, compare_key)
				updatei(records[i][0],table_name,compare_key)
		else:
			continue

	



