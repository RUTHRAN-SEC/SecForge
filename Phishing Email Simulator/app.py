from flask import Flask, request, render_template
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Initialize database
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clicks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT,
            time TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Phishing simulation link
@app.route("/offer")
def offer():
    email = request.args.get("user")

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clicks (email, time) VALUES (?, ?)",
                   (email, str(datetime.now())))
    conn.commit()
    conn.close()

    return render_template("landing.html")


# Admin report page
@app.route("/report")
def report():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clicks")
    data = cursor.fetchall()
    conn.close()

    return render_template("report.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
