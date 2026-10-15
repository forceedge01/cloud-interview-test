import os
import pymysql
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from orm.database import create_db_engine
from orm.user import User
from sqlalchemy import select
from sqlalchemy.orm import Session

load_dotenv()

# Objective is to retrieve a user from the database by ID 
# along with their role and permissions.

app = Flask(__name__)
API_TOKEN = os.environ["API_TOKEN"]


engine = create_db_engine()

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    connection = None

    try:
        auth = request.headers.get("Authorization", "")
        token = auth.replace("Bearer ", "")

        if token != API_TOKEN:
            return jsonify({"error": "Unauthorized"}), 500

        with Session(engine) as session:
            stmt = select(User).where(User.id == user_id)
            user = session.execute(stmt).scalar_one_or_none()

            if not user:
                return jsonify({"error": "User not found"}), 500

            return jsonify({
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "permissions": [permission.permission_name for permission in user.permissions]
            })

    except Exception as e:
        return jsonify({"error": f"Request failed, {str(e)}"}), 500
    finally:
        if connection:
            connection.close()

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
