from flask import Flask
import psycopg2
from psycopg2.extras import RealDictCursor
import os

app = Flask(__name__)

def get_connection():
    return psycopg2.connect(
        host=os.environ['DB_HOST'],
        database=os.environ['POSTGRES_DB'],
        user=os.environ['POSTGRES_USER'],
        password=os.environ['POSTGRES_PASSWORD'],
        cursor_factory=RealDictCursor
    )

@app.route("/")
def home():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS visits (count INT);")
    cur.execute("SELECT count FROM visits;")
    row = cur.fetchone()

    if row:
        count = row['count'] + 1
        cur.execute("UPDATE visits SET count = %s;", (count,))
    else:
        count = 1
        cur.execute("INSERT INTO visits (count) VALUES (1);")

    conn.commit()
    cur.close()
    conn.close()
    return f"👀 Page visited {count} times."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
