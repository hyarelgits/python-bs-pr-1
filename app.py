from flask import Flask, render_template, request
import sqlite3
import logging
import os

# Create logs folder automatically
os.makedirs("logs", exist_ok=True)

# Configure logging
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

app = Flask(__name__)


@app.route("/")
def home():

    return render_template("index.html")

@app.route("/students")
def students():

    conn = sqlite3.connect("students.db")

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students"
    )

    rows = cursor.fetchall()

    conn.close()

    return render_template(
        "students.html",
        rows=rows
    )




@app.route("/add", methods=["GET", "POST"])
def add_student():

    if request.method == "POST":

        name = request.form["name"]
        marks = request.form["marks"]

        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO students(name, marks) VALUES (?, ?)",
            (name, marks)
        )

        conn.commit()
        conn.close()

        logging.info(
            f"Student Added | Name={name} | Marks={marks}"
        )

        return "Student Saved"

    return render_template("add_student.html")

@app.route("/search", methods=["GET"])
def search():

    name = request.args.get("name")

    if not name:

        return render_template(
            "search.html"
        )

    conn = sqlite3.connect(
        "students.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE name=?",
        (name,)
    )

    rows = cursor.fetchall()

    conn.close()

    return str(rows)



if __name__ == "__main__":

    logging.info("Application Started")

    app.run(debug=True)
