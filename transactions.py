from db import get_db_connection


def add_transaction(user_id, t_type, category, amount, date):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO transactions (user_id, type, category, amount, date) VALUES (%s, %s, %s, %s, %s)",
                       (user_id, t_type, category, amount, date))
        conn.commit()
        print(f"{t_type.capitalize()} added successfully.")
    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()
def view_transactions(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM transactions WHERE user_id = %s", (user_id,))
        transactions = cursor.fetchall()
        for transaction in transactions:
            print(transaction)
    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()
def delete_transaction(user_id, transaction_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM transactions WHERE id = %s AND user_id = %s", (transaction_id, user_id))
        conn.commit()
        print(f"Transaction with ID {transaction_id} deleted successfully.")
    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()
