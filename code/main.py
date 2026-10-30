import os
import pymysql
from flask import Flask, request, jsonify

app = Flask(__name__)

# DB Structure of the user table:
# CREATE TABLE users (
#     id INT AUTO_INCREMENT,
#     username VARCHAR(255) NOT NULL,
#     email VARCHAR(255) NOT NULL,
#     password VARCHAR(255) NULL
# );

# DB Structure of the roles table:
# CREATE TABLE roles (
#     id INT AUTO_INCREMENT,
#     role_name VARCHAR(100) NOT NULL,
#     permissions JSON(250) NOT NULL,
# );

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/users/")
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

    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)
    user_row = cursor.fetchone()

    if not user_row:
        return jsonify({"error": "User not found"}), 500

    return jsonify(user_row), 200

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
