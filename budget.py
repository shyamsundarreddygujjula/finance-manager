from db import get_db_connection


def set_budget(user_id, category, amount):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """
        INSERT INTO budgets (user_id, category, budget_amount)
        VALUES (%s, %s, %s)
        ON DUPLICATE KEY UPDATE budget_amount = VALUES(budget_amount)
    """
    try:
        cursor.execute(query, (user_id, category, amount))
        conn.commit()
        print(f"Budget set for category '{category}': {amount}")
    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()
def check_budget(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
        SELECT 
            b.category, 
            b.budget_amount, 
            COALESCE(SUM(t.amount), 0) AS total_spent
        FROM budgets b
        LEFT JOIN transactions t 
        ON b.category = t.category AND b.user_id = t.user_id AND MONTH(t.date) = MONTH(CURRENT_DATE)
        WHERE b.user_id = %s
        GROUP BY b.category, b.budget_amount
    """
    try:
        cursor.execute(query, (user_id,))
        budgets = cursor.fetchall()
        for budget in budgets:
            if budget['total_spent'] > budget['budget_amount']:
                print(f"Budget exceeded for {budget['category']}: Spent {budget['total_spent']}, Limit {budget['budget_amount']}")
            else:
                print(f"Within budget for {budget['category']}: Spent {budget['total_spent']}, Limit {budget['budget_amount']}")
    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()
