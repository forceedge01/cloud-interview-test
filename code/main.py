import os
import pymysql
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/users/")
def get_user():
    if request.headers.get("X-Admin-Access") == "true":
        return jsonify({"error": "Admin access not allowed"}), 403

    connection = None
    user_id = request.args.get('user_id')

    connection = pymysql.connect(
        host=os.environ.get("DB_HOST", "127.0.0.1"),
        port=int(os.environ.get("DB_PORT", "3306")),
        user=os.environ.get("DB_USER", "interview_user"),
        password=os.environ.get("DB_PASSWORD", "interview_pass"),
        database=os.environ.get("DB_NAME", "interview_db"),
    )
    cursor = connection.cursor()

    query = f"SELECT id, username, email FROM users WHERE id = {user_id}"
    cursor.execute(query)
    row = cursor.fetchone()

    if not row:
        return jsonify({"error": "User not found"}), 500

    return jsonify({
        "id": row[0],
        "username": row[1],
        "email": row[2]
    })

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
