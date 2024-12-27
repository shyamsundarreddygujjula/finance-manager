import mysql.connector 

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",           # Your MySQL server hostname, usually localhost
        user="root",       # Your MySQL username
        password="********",   # Your MySQL password
        database="finance_manager", # Your database name
        auth_plugin="mysql_native_password" # Use this if you face authentication issues with MySQL
    )