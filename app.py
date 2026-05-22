from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error
import os
import re

app = Flask(__name__)
CORS(app)

# =========================
# BASE DIRECTORY
# =========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# =========================
# DATABASE CONFIG
# =========================
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "ganesh@123",
    "database": "portfolio_db"
}

# =========================
# DB CONNECTION
# =========================
def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

# =========================
# EMAIL VALIDATION
# =========================
def is_valid_email(email):
    pattern = r'^[\w\.\+\-]+@[\w\-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

# =========================
# PORTFOLIO WEBSITE
# =========================
@app.route("/")
def portfolio():
    return send_from_directory(BASE_DIR, "index.html")

# =========================
# ADMIN PANEL
# =========================
@app.route("/admin")
def admin():
    return send_from_directory(BASE_DIR, "admin.html")

# =========================
# SERVE FILES
# =========================
@app.route('/<path:filename>')
def serve_files(filename):
    return send_from_directory(BASE_DIR, filename)

# =========================
# CONTACT FORM
# =========================
@app.route("/contact", methods=["POST"])
def contact():

    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "message": "No data received"
        }), 400

    first_name = data.get("first_name", "").strip()
    last_name = data.get("last_name", "").strip()
    email = data.get("email", "").strip()
    subject = data.get("subject", "").strip()
    message = data.get("message", "").strip()

    if not first_name:
        return jsonify({
            "success": False,
            "message": "First name is required"
        }), 400

    if not email:
        return jsonify({
            "success": False,
            "message": "Email is required"
        }), 400

    if not is_valid_email(email):
        return jsonify({
            "success": False,
            "message": "Invalid email address"
        }), 400

    if not message:
        return jsonify({
            "success": False,
            "message": "Message is required"
        }), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        sql = """
        INSERT INTO contacts
        (
            first_name,
            last_name,
            email,
            subject,
            message
        )
        VALUES (%s,%s,%s,%s,%s)
        """

        values = (
            first_name,
            last_name,
            email,
            subject,
            message
        )

        cursor.execute(sql, values)
        conn.commit()

        return jsonify({
            "success": True,
            "message": "Message sent successfully!"
        })

    except Error as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 500

    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass

# =========================
# GET CONTACTS
# =========================
@app.route("/contacts", methods=["GET"])
def get_contacts():

    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
            SELECT *
            FROM contacts
            ORDER BY submitted_at DESC
        """)

        contacts = cursor.fetchall()

        return jsonify({
            "success": True,
            "count": len(contacts),
            "data": contacts
        })

    except Error as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 500

    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass

# =========================
# DELETE CONTACT
# =========================
@app.route("/contacts/<int:id>", methods=["DELETE"])
def delete_contact(id):

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM contacts WHERE id=%s",
            (id,)
        )

        conn.commit()

        return jsonify({
            "success": True,
            "message": "Contact deleted successfully"
        })

    except Error as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 500

    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass

# =========================
# ADMIN LOGIN
# =========================
@app.route("/admin/login", methods=["POST"])
def admin_login():

    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if username == "admin" and password == "admin123":
        return jsonify({
            "success": True,
            "message": "Login successful"
        })

    return jsonify({
        "success": False,
        "message": "Invalid username or password"
    }), 401

# =========================
# RUN APP
# =========================
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )