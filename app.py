# INTENTIONALLY VULNERABLE - EDUCATIONAL LAB ONLY
# Do not deploy this application.

from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route("/users")
def find_user():
    username = request.args.get("username", "")

    connection = sqlite3.connect(":memory:")
    connection.execute("CREATE TABLE users (username TEXT)")
    connection.execute("INSERT INTO users VALUES ('student')")

    # FIXED: SQL injection prevented using parameterized query
   query = "SELECT username FROM users WHERE username = ?"
rows = connection.execute(query, (username,)).fetchall()

    connection.close()
    return {"users": [row[0] for row in rows]}
