import sqlite3
import pandas as pd

# Connect to your local SQLite DB
conn = sqlite3.connect("mma_sim.db")

def print_result(title, query):
    print(f"\n🔍 {title}")
    try:
        df = pd.read_sql(query, conn)
        if df.empty:
            print("✅ No issues found.")
        else:
            print(df)
    except Exception as e:
        print(f"[!] Error: {e}")

# 1. Fighters with no public attributes
print_result(
    "Fighters missing from fighter_attributes:",
    '''
    SELECT w.worker_id, w.worker_name
    FROM Workers w
    LEFT JOIN fighter_attributes fa ON w.worker_id = fa.worker_id
    WHERE w.Role = 'fighter' AND fa.worker_id IS NULL
    '''
)

# 2. Fighters with no hidden attributes
print_result(
    "Fighters missing from fighter_hidden_attributes:",
    '''
    SELECT w.worker_id, w.worker_name
    FROM Workers w
    LEFT JOIN fighter_hidden_attributes fh ON w.worker_id = fh.worker_id
    WHERE w.Role = 'fighter' AND fh.worker_id IS NULL
    '''
)

# 3. Titles with no history
print_result(
    "Titles with no entry in Title_Histories:",
    '''
    SELECT b.title_id
    FROM Title_Belts b
    LEFT JOIN Title_Histories h ON b.title_id = h.title_id
    WHERE h.title_id IS NULL
    '''
)

# 4. Titles with no pre-game history
print_result(
    "Titles with no entry in Title_Histories_PreGame:",
    '''
    SELECT b.title_id
    FROM Title_Belts b
    LEFT JOIN Title_Histories_PreGame p ON b.title_id = p.title_id
    WHERE p.title_id IS NULL
    '''
)

# 5. Worker absences without a valid worker
print_result(
    "Worker_Absences without a valid worker in Workers:",
    '''
    SELECT a.worker_id
    FROM Worker_Absences a
    LEFT JOIN Workers w ON a.worker_id = w.worker_id
    WHERE w.worker_id IS NULL
    '''
)

conn.close()
print("\n✅ Validation complete.")
