import os
import pandas as pd
import sqlite3

DATA_FOLDER = r"C:\Users\cptjo\Dropbox\Raw DB Files\Alpha DB"
DB_NAME = "mma_sim.db"


use_sqlite = True
conn = sqlite3.connect(DB_NAME) if use_sqlite else None

# 🧠 Store loaded tables in a dictionary
loaded_tables = {}

# 📂 Load each .csv or .xlsx file
for file in os.listdir(DATA_FOLDER):
    if file.endswith(".csv"):
        file_path = os.path.join(DATA_FOLDER, file)
        table_name = os.path.splitext(file)[0]  # e.g., "fighter_attributes"

        try:
            if file.endswith(".csv"):
                df = pd.read_csv(file_path)
            else:
                df = pd.read_excel(file_path)

            loaded_tables[table_name] = df

            if use_sqlite:
                df.to_sql(table_name, conn, if_exists="replace", index=False)
                print(f"[✓] Loaded into DB: {table_name}")

            else:
                print(f"[✓] Loaded into memory: {table_name}")

        except Exception as e:
            print(f"[X] Failed to load {file}: {e}")

if use_sqlite:
    conn.commit()
    conn.close()

print(f"\n✅ Loaded {len(loaded_tables)} tables.")
