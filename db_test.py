import sqlite3
import pandas as pd

# Connect to your SQLite database file
conn = sqlite3.connect("mma_sim.db")

# List all tables
print("✅ Available Tables:")
tables = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table';", conn)
print(tables)

# Try previewing the Workers table
try:
    df = pd.read_sql("SELECT * FROM Workers LIMIT 10;", conn)
    print("\n🧍 Workers Preview:")
    print(df)
except Exception as e:
    print("\n[!] Could not query Workers table:")
    print(e)

conn.close()
