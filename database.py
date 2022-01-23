from getpass import getpass
import mysql.connector


class database:
     
     def __init__(self, hostname, database_name, username, password):
          self.hostname = hostname
          self.database_name = database_name
          self.username = username
          self.password = password
          existence = self.existence()
          # table = self.table()
     
     def create_database(self):
          conn = mysql.connector.connect(host=self.hostname, username=self.username, password=self.password)
          cursor = conn.cursor()
          # cursor.execute("USE "+self.database_name)
          cursor.execute("SHOW DATABASES")
          # query = cursor.fetchall()
          # print([item[0] for item in query])
          result = cursor.fetchall()
          database_list = [item[0] for item in result] #conversion to list of str``
          cond = self.existence.check_existence(database_list, self.database_name)
          if cond == True:
               print(self.database_name, " database exists")
          else:
               print(self.database_name, "database doesn't exist")
               # database_name = input("Enter your new database name:: ")
               self.existence.create_database(conn, self.database_name)
     
     def create_table(self, conn, table_name):
          cursor = conn.cursor()
          cursor.execute("USE "+self.database_name)
          cursor.execute("SHOW TABLES")
          result = cursor.fetchall()
          table_list = [item[0] for item in result] #conversion to list of str
          cond = self.existence.check_existence(table_list, table_name)
          if cond == True:
               print(table_name, "table already exists")
               cursor.execute("DESCRIBE "+table_name)
               structure = cursor.fetchall()
               print([item[0] for item in structure])
               
          else:
               print(table_name, "table doesn't exists")
               # table_name = input("Enter your new table name:: ")
               create_table_query = input(f'Enter your query to create structure of {table_name} table:: \n')
               self.existence.create_table_query(conn, table_name, create_table_query)
     
     def insert_into_table(self, sql):
          cursor = conn.cursor()
          cursor.execute(sql)
          conn.commit()
     
     class existence:
          
          def check_existence(list_data, data_dt):
               for data in list_data:
                    if data == data_dt:
                         return True
                    
               return False 
          
          def create_database(conn, database_name):
               cursor = conn.cursor()
               cursor.execute("CREATE DATABASE "+database_name)
               print("Loading........................")
               print(database_name, "database created")
          
          def create_table_query(conn, table_name, table_query):
               cursor = conn.cursor()
               cursor.execute(table_query)
               print("Loading........................")
               print(table_name, "table created")
               cursor.execute("DESCRIBE "+table_name)
               structure = cursor.fetchall()
               print([item[0] for item in structure])
               
     
          

if __name__ == '__main__':
     hostname = input("Host Name:: ")
     database_name = input("Database Name:: ")
     username = input("User Name:: ")
     password = getpass("Enter password:: ")
     conn = mysql.connector.connect(host=hostname, username=username, password=password)
     obj = database(hostname, database_name, username, password)
     obj.create_database()
     table_name = input("Enter your table name:: ")
     """
     CREATE TABLE bhandari(id INT NOT NULL AUTO_INCREMENT, fname VARCHAR(45) NOT NULL, mname VARCHAR(45) NULL, lname VARCHAR(45) NOT NULL, address VARCHAR(45) NOT NULL, contact VARCHAR(45) NOT NULL, dob DATETIME NOT NULL, PRIMARY KEY (id));
     """
     obj.create_table(conn, table_name)
     sql = input(f'Enter your insert query to insert data into {table_name} table:: \n')
     """
     INSERT INTO bhandari(fname, mname, lname, address, contact, dob) VALUES ("Keshav", "", "Bhandari", "Butwal", "9869260495", "1999-08-10")
     """
     obj.insert_into_table(sql)
     
    