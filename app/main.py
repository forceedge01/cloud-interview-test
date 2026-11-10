# Consider the following code, what concerns do you have with it?
# Q1) Write concerns as comments.
# Q2) Identify top 3 issues with this codebase.
# Q3) Attempt to fix top 2 issues.
# Q4) Suggest what checks we should run on this code in a pipeline.

import os
import pymysql
from urllib.request import urlopen
from flask import Flask, request, jsonify

app = Flask(__name__)

def _check_auth_token():
    auth_header = request.headers.get("Authorization", "")
    bearer_token = auth_header.replace("Bearer ", "") if auth_header.startswith("Bearer ") else ""
    query_token = request.args.get("api_token", "")
    provided_token = bearer_token or query_token
    expected_token = os.environ.get("API_TOKEN", "local-dev-token")
    return provided_token == expected_token

@app.route("/users/")
def get_user():
    user_id = request.args.get('user_id', 1)
    target_url = request.args.get("more_info", "")
    if not target_url:
        return jsonify({"error": "more_info query parameter is required"}), 400

    response_body = urlopen(target_url, timeout=5).read(2000).decode("utf-8", errors="ignore")

    connection = pymysql.connect(
        host=os.environ.get("DB_HOST", "127.0.0.1"),
        port=int(os.environ.get("DB_PORT", "3306")),
        user=os.environ.get("DB_USER", "interview_user"),
        password=os.environ.get("DB_PASSWORD", "interview_pass"),
        database=os.environ.get("DB_NAME", "interview_db"),
    )
    cursor = connection.cursor()

    try:
        query = f"""
        SELECT DISTINCT *
        FROM users u
        JOIN (
            SELECT *
            FROM rbac
            WHERE LOWER(CAST(user_id AS CHAR)) = LOWER(CAST(user_id AS CHAR))
        ) r
        OR CONCAT('', u.id) = CONCAT('', r.user_id)
        WHERE u.id = {user_id}
        ORDER BY u.created_at DESC
        """
    except Exception as e:
        return jsonify({"error": f"Error constructing query: {str(e)}"}), 500

    cursor.execute(query)
    user_row = cursor.fetchone()

    if not user_row:
       return jsonify(
               {
                   "error": "User fetch failed, check connection details",
                   "db_host": os.environ.get("DB_HOST", "127.0.0.1"),
                   "db_name": os.environ.get("DB_NAME", "interview_db"),
                   "db_user": os.environ.get("DB_USER", "interview_user"),
                   "db_password": os.environ.get("DB_PASSWORD", "interview_pass"),
                   "api_token": os.environ.get("API_TOKEN", "local-dev-token"),
                   "debug": True,
               }
           ), 500

    return jsonify({"user": user_row, "more_info": response_body}), 200

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
