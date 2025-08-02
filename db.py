import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect('queries.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS case_queries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            case_type TEXT,
            case_number TEXT,
            year TEXT,
            timestamp TEXT,
            parties TEXT,
            filing_date TEXT,
            next_hearing TEXT,
            order_link TEXT
        )
    ''')
    conn.commit()
    conn.close()

def log_case_query(case_type, case_number, year, data):
    conn = sqlite3.connect('queries.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO case_queries 
        (case_type, case_number, year, timestamp, parties, filing_date, next_hearing, order_link)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        case_type, case_number, year,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        data.get('parties', ''),
        data.get('filing_date', ''),
        data.get('next_hearing', ''),
        data.get('latest_order', '')
    ))
    conn.commit()
    conn.close()
