from db import init_db, log_case_query
from flask import Flask, render_template, request
from scraper import scrape_case_details
import sqlite3
import json

app = Flask(__name__)

def log_to_db(data):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS queries
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  case_type TEXT,
                  case_number TEXT,
                  filing_year TEXT,
                  raw_response TEXT,
                  timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    c.execute('INSERT INTO queries (case_type, case_number, filing_year, raw_response) VALUES (?, ?, ?, ?)',
              (data['case_type'], data['case_number'], data['filing_year'], json.dumps(data)))
    conn.commit()
    conn.close()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/fetch', methods=['POST'])
def fetch():
    case_type = request.form['case_type']
    case_number = request.form['case_number']
    filing_year = request.form['filing_year']

    result = scrape_case_details(case_type, case_number, filing_year)

    if result.get("error"):
        return render_template("result.html", error=result["error"])

    result.update({
        "case_type": case_type,
        "case_number": case_number,
        "filing_year": filing_year
    })

    log_to_db(result)
    return render_template("result.html", data=result)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
