import os
import hmac
from socket import create_connection
from flask import Flask, request, jsonify

# Objective is to retrieve a user from the database by ID 
# along with their role and permissions.

app = Flask(__name__)
API_TOKEN = os.environ["API_TOKEN"]

def is_authenticated():
    auth = request.headers.get("Authorization", "")

    if not auth.startswith("Bearer "):
        return False

    token = auth.split(" ", 1)[1]
    return hmac.compare_digest(token, API_TOKEN)

@app.route("/users/<int:user_id>", methods=["GET"])

def get_user(user_id):
    if not is_authenticated():
        return jsonify({"error": "Unauthorized"}), 401

    try:
        user = get_user_from_db(user_id)
        if user is None:
            return jsonify({"error": "User not found"}), 404
        return jsonify(user)

    except Exception:
        # Log the actual error internally, but don't expose DB details.
        app.logger.exception("Error while fetching user")

        return jsonify({"error": "Internal server error"}), 500

def get_user_from_db(user_id):
    connection = create_connection(
        os.environ["DB_USERNAME"],
        os.environ["DB_PASSWORD"]
    )

    try:
        # Use a parameterized query instead of putting user_id
        # directly into the SQL string.
        cursor = connection.execute(
            """
            SELECT id, username, email
            FROM users
            WHERE id = ?
            """,
            (user_id,)
        )

        row = cursor.fetchone()

        if not row:
            return None

        return {
            "id": row[0],
            "username": row[1],
            "email": row[2]
        }

    finally:
        connection.close()

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
