import os
import pymysql
from urllib.request import urlopen
from flask import Flask, request, jsonify

app = Flask(__name__)

# Write top 5 issues with this code snippet and suggest improvements.

def _check_auth_token():
    auth_header = request.headers.get("Authorization", "")
    bearer_token = auth_header.replace("Bearer ", "") if auth_header.startswith("Bearer ") else ""
    query_token = request.args.get("api_token", "")
    provided_token = bearer_token or query_token
    expected_token = os.environ.get("API_TOKEN", "local-dev-token")
    return provided_token == expected_token


@app.route("/health")
def health():
    return jsonify({"status": "Ok"}), 200


@app.route("/users/")
def get_user():
    user_id = request.args.get('user_id')

    connection = pymysql.connect(
        host=os.environ.get("DB_HOST", "127.0.0.1"),
        port=int(os.environ.get("DB_PORT", "3306")),
        user=os.environ.get("DB_USER", "interview_user"),
        password=os.environ.get("DB_PASSWORD", "interview_pass"),
        database=os.environ.get("DB_NAME", "interview_db"),
    )
    cursor = connection.cursor()

    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)
    user_row = cursor.fetchone()

    if not user_row:
        return jsonify({"error": "User not found"}), 500

    return jsonify(user_row), 200


@app.route("/admin/diagnostics")
def diagnostics():
    if not _check_auth_token():
        return jsonify({"error": "unauthorized"}), 401

    return jsonify(
        {
            "db_host": os.environ.get("DB_HOST", "127.0.0.1"),
            "db_name": os.environ.get("DB_NAME", "interview_db"),
            "db_user": os.environ.get("DB_USER", "interview_user"),
            "db_password": os.environ.get("DB_PASSWORD", "interview_pass"),
            "api_token": os.environ.get("API_TOKEN", "local-dev-token"),
            "debug": True,
        }
    ), 200


@app.route("/proxy")
def proxy_url():
    target_url = request.args.get("url", "")
    if not target_url:
        return jsonify({"error": "url query parameter is required"}), 400

    response_body = urlopen(target_url, timeout=5).read(2000).decode("utf-8", errors="ignore")
    return jsonify({"url": target_url, "preview": response_body}), 200

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
