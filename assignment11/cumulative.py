#Task 2: A Line Plot with Pandas 
import pandas as pd 
import sqlite3 
import matplotlib.pyplot as plt

conn = sqlite3.connect("../db/lesson.db")

sql = """
    SELECT 
        o.order_id,
        SUM(p.price * l.quantity) AS total_price
    FROM orders o
    JOIN line_items l
        ON o.order_id = l.order_id
    JOIN products p
        ON l.product_id = p.product_id
    GROUP BY o.order_id
    ORDER BY o.order_id
"""

#Load database 
df = pd.read_sql_query(sql, conn)
print("Order Revenue Data:")
print(df, "\n")

#Cumulative function 
def cumulative(row):
   totals_above = df['total_price'][0:row.name+1]
   return totals_above.sum()

df['cumulative'] = df.apply(cumulative, axis=1)

#Plot using Line Plot 
plt.figure(figsize=(10, 6))
plt.plot(df["order_id"], df["cumulative"], marker="o", color="purple")

plt.title("Cumulative Revenue Over Time")
plt.xlabel("Order ID")
plt.ylabel("Cumulative Revenue $")
plt.grid(True)

plt.tight_layout()
plt.show()