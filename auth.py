import bcrypt
from db import get_db_connection

def register_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
        conn.commit()
        print("Registration successful!")
    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()
def login_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()
        if user and bcrypt.checkpw(password.encode(), user['password'].encode()):
            print("Login successful!")
            return user['id']
        else:
            print("Invalid username or password.")
            return None
    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()
