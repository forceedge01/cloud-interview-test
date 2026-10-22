import os
import pymysql
from flask import Flask, request, jsonify

# Objective is to retrieve a user from the database by ID 
# along with their role and permissions.

app = Flask(__name__)
API_TOKEN = os.environ["API_TOKEN"]

# Health endpoint for AWS.
@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/users/", methods=["GET"])
def get_user():
    connection = None

    user_id = request.args.get('user_id')
    auth = request.headers.get("Authorization", "")
    token = auth.replace("Bearer ", "")

    if token != API_TOKEN:
        return jsonify({"error": "Unauthorized"}), 500

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
