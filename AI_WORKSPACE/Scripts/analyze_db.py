#!/usr/bin/env python3
import sqlite3
import os

db_path = 'S:\\home-assistant_v2.db'
if os.path.exists(db_path):
    size_mb = os.path.getsize(db_path) / (1024 * 1024)
    print(f'Database size: {size_mb:.1f} MB')

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('SELECT name FROM sqlite_master WHERE type="table"')
    tables = cursor.fetchall()

    print('Table sizes:')
    total_rows = 0
    for table in tables:
        table_name = table[0]
        try:
            cursor.execute(f'SELECT COUNT(*) FROM {table_name}')
            count = cursor.fetchone()[0]
            total_rows += count
            print(f'  {table_name}: {count} rows')
        except Exception as e:
            print(f'  {table_name}: Error - {e}')

    print(f'Total rows across all tables: {total_rows}')
    conn.close()
else:
    print('Database file not found')