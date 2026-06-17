#Task 1: Plotting with Pandas 
import pandas as pd 
import sqlite3 
import matplotlib.pyplot as plt 

conn = sqlite3.connect("../db/lesson.db")

#SQL query
sql = """
    SELECT 
    last_name, 
    SUM(price * quantity) AS revenue 
    FROM employees e 
    JOIN orders o 
        ON e.employee_id = o.employee_id 
    JOIN line_items l 
        ON o.order_id = l.order_id 
    JOIN products p 
        ON l.product_id = p.product_id 
    GROUP BY e.employee_id;
"""
#Load database
employee_results = pd.read_sql_query(sql, conn)
print("Employee Revenue Data:")
print(employee_results, "\n")

#Plot using Pandas 
plt.figure(figsize=(10, 6))
plt.bar(employee_results["last_name"], employee_results["revenue"], color="blue")

plt.title("Employee Revenue Performance")
plt.xlabel("Employee Last Name")
plt.ylabel("Total Revenue $")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()