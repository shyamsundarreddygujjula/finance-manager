import os


def backup_data():
    try:
        file_name = "backup.sql"
        db_config = {
            "host": "localhost",
            "user": "root",
            "password": "********",
            "database": "finance_manager"
        }
        cmd = f"mysqldump -h {db_config['host']} -u {db_config['user']} -p{db_config['password']} {db_config['database']} > {file_name}"
        os.system(cmd)
        print(f"Backup successful! Data saved in {file_name}")
    except Exception as e:
        print("Error during backup:", e)
def restore_data():
    try:
        file_name = "backup.sql"
        db_config = {
            "host": "localhost",
            "user": "root",
            "password": "********",
            "database": "finance_manager"
        }
        cmd = f"mysql -h {db_config['host']} -u {db_config['user']} -p{db_config['password']} {db_config['database']} < {file_name}"
        os.system(cmd)
        print("Restore successful! Data restored from backup.sql")
    except Exception as e:
        print("Error during restore:", e)