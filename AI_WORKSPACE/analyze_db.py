import sqlite3
import os

def analyze_ha_database(db_path):
    if not os.path.exists(db_path):
        print(f"Database file not found: {db_path}")
        return

    file_size = os.path.getsize(db_path) / (1024 * 1024 * 1024)  # GB
    print(f"Database Size: {file_size:.2f} GB")
    print("=" * 50)

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Get all tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()

    print("Table Row Counts:")
    print("-" * 30)
    total_rows = 0
    for table in tables:
        table_name = table[0]
        try:
            cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
            count = cursor.fetchone()[0]
            total_rows += count
            print(f"{table_name}: {count:,} rows")
        except Exception as e:
            print(f"{table_name}: Error - {e}")

    print(f"\nTotal rows across all tables: {total_rows:,}")

    # Check states table specifically (usually the largest)
    try:
        cursor.execute("SELECT COUNT(*) FROM states")
        states_count = cursor.fetchone()[0]
        print(f"\nStates table: {states_count:,} rows")

        # Get entity breakdown
        cursor.execute("""
            SELECT entity_id, COUNT(*) as count
            FROM states
            GROUP BY entity_id
            ORDER BY count DESC
            LIMIT 20
        """)
        print("\nTop 20 entities by state changes:")
        print("-" * 40)
        for row in cursor.fetchall():
            print(f"{row[0]}: {row[1]:,} changes")

    except Exception as e:
        print(f"Error analyzing states table: {e}")

    conn.close()

if __name__ == "__main__":
    analyze_ha_database("S:/home-assistant_v2.db")