import pymysql

Connection = pymysql.connect(host="localhost", user="root", password=" ", db="python_chat")  # 密码隐去了

cursor = Connection.cursor()
sql_create_table = '''

    create table user_information
     (
      user_name varchar (20),
      
      password varchar (20),
      
      data LONGBLOB
    )

'''
cursor.execute(sql_create_table)
cursor.close()
