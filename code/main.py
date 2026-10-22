import os
import pymysql
from flask import Flask, request, jsonify

# This script exposes:
# - GET /health for a basic health check
# - GET /users/?user_id=<id> with Bearer token auth, then fetches a user row from MySQL
#
# Exercise objective:
# Materially improve the application quality as much as possible
# (security, correctness, resilience, and maintainability).
#
# Part 1 challenge focus:
# - Implement GET /users/<id>
# - Enforce bearer-token auth
# - Return user data with RBAC role and permissions
#
# Target end-state behavior:
# The API should be callable as:
# curl -H "Authorization: Bearer ${API_TOKEN}" http://localhost:5000/users/1

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
