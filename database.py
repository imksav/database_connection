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
          result = cursor.fetchall()
          database_list = [item[0] for item in result] #conversion to list of str
          cond = self.existence.check_existence(database_list, self.database_name)
          if cond == True:
               print(self.database_name, "exists")
          else:
               print(self.database_name, "doesn't exist")
               database_name = input("Enter your new database name:: ")
               self.existence.create_database(conn, database_name)
     
     def create_table(self, conn, table_name):
          cursor = conn.cursor()
          cursor.execute("USE "+self.database_name)
          cursor.execute("SHOW TABLES")
          result = cursor.fetchall()
          table_list = [item[0] for item in result] #conversion to list of str
          cond = self.existence.check_existence(table_list, table_name)
          if cond == True:
               print(table_name, "already exists")
          else:
               print(table_name, "doesn't exists")
               table_name = input("Enter your new table name:: ")
               create_table_query = input("Enter your query to create table name:: ")
               self.existence.create_table_query(conn, create_table_query)
     
     def insert_into_table(self, sql):
          cursor = conn.cursor()
          # cursor.execute(sql, value)
          cursor.execute(sql)
          conn.commit()
     
     class existence:
          
          def check_existence(list_data, data_dt):
               for data in list_data:
                    if data == data_dt:
                         return True
                    
               return False 
          
          def check_table(table_list, table_name):
               for db_name in database_list:
                    if db_name == database_name:
                         return True
                    
               return False
          
          def create_database(conn, database_name):
               cursor = conn.cursor()
               cursor.execute("CREATE DATABASE "+database_name)
               print(database_name, " created")
          
          def create_table_query(conn, table_query):
               cursor = conn.cursor()
               cursor.execute(table_query)
               
     
          

if __name__ == '__main__':
     hostname = input("Host Name:: ")
     database_name = input("Database Name:: ")
     username = input("User Name:: ")
     password = getpass("Enter password:: ")
     
     conn = mysql.connector.connect(host=hostname, username=username, password=password) # make a function in utility
     obj = database(hostname, database_name, username, password)
     obj.create_database()
     table_name = input("Enter your table name:: ")
     obj.create_table(conn, table_name)
     sql = input("Enter your insert query:: ")
     value = input("Enter your value:: ")
     obj.insert_into_table(sql)
     
    