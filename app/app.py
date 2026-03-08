from flask import Flask
import psycopg2
import os

app = Flask(__name__)

# Read database settings from environment variables
DB_HOST = os.getenv("DB_HOST", "postgres")
DB_NAME = os.getenv("POSTGRES_DB", "devopsdb")
DB_USER = os.getenv("POSTGRES_USER", "devops")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "Shazam2003")

@app.route("/")
def home():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )

        conn.close()

        return "Flask connected to PostgreSQL successfully!"

    except Exception as e:
        return f"Database connection failed: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
