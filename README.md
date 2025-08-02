# Court-Data Fetcher & Mini-Dashboard

## 🔍 Court Targeted
Faridabad District Court - https://districts.ecourts.gov.in/faridabad

## 💻 Tech Stack
- Frontend: HTML + Flask templates
- Backend: Python (Flask)
- Scraper: Playwright + BeautifulSoup
- DB: SQLite

## 🧠 CAPTCHA Handling
Currently using mock data. Scraper will use Playwright for bypassing view-state/CAPTCHA where needed.

## 🚀 How to Run
```bash
pip install -r requirements.txt
playwright install
python app.py
