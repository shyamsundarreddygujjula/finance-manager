from db import get_db_connection


def generate_report(user_id, period='monthly'):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
        SELECT type, category, SUM(amount) AS total
        FROM transactions
        WHERE user_id = %s AND 
        (MONTH(date) = MONTH(CURRENT_DATE) AND YEAR(date) = YEAR(CURRENT_DATE))
        GROUP BY type, category
    """ if period == 'monthly' else """
        SELECT type, category, SUM(amount) AS total
        FROM transactions
        WHERE user_id = %s AND YEAR(date) = YEAR(CURRENT_DATE)
        GROUP BY type, category
    """
    try:
        cursor.execute(query, (user_id,))
        report = cursor.fetchall()
        for row in report:
            print(row)
    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()
def calculate_savings(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT type, SUM(amount) AS total FROM transactions WHERE user_id = %s GROUP BY type", (user_id,))
        data = cursor.fetchall()
        income = sum(row['total'] for row in data if row['type'] == 'income')
        expenses = sum(row['total'] for row in data if row['type'] == 'expense')
        print(f"Savings: Income ({income}) - Expenses ({expenses}) = {income - expenses}")
    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()