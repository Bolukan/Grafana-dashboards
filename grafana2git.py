import json
import os
import sqlite3

# Import the variables from config.py
# DATABASE_PATH = '/var/lib/docker/volumes/<volume>/_data/grafana.db'
# FILE_PATH = '~/Grafana-dashboards/dashboard/'
from config import DATABASE_PATH, FILE_PATH

def fetch_data():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT slug, data FROM dashboard LIMIT 100")
        data = cursor.fetchall()
        return data
    finally:
        conn.close()

def post_to_map(data):
    os.makedirs(FILE_PATH, exist_ok=True)

    for slug, content in data:
        safe_slug = "".join(c for c in slug if c.isalnum() or c in ('-', '_')).strip()

        try:
            if isinstance(content, bytes):
                content = content.decode('utf-8')
            json_content = json.loads(content)
            pretty_content = json.dumps(json_content, indent=4)
            file_path = os.path.join(FILE_PATH, f"{safe_slug}.json")
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(pretty_content)

        except (json.JSONDecodeError, UnicodeDecodeError):
            print(f"Invalid JSON for slug {slug}, skipping.")
            continue
        
    print(f"Saved {len(data)} records to {FILE_PATH}")
   
def main():
    data = fetch_data()
    post_to_map(data)

if __name__ == "__main__":
    main()