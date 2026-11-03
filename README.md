# 🎓 Student Management Portal

A Flask-based Student Management System built using Python, SQLite, HTML, Bootstrap, Git, GitHub, Docker, and Linux.

---

# 🏗 Project Architecture

```text
+---------+
| Browser |
+---------+
     |
     v
+-------------------+
| HTML Templates    |
|-------------------|
| index.html        |
| add_student.html  |
| students.html     |
| search.html       |
| login.html        |
+-------------------+
     |
     v
+-------------------+
| Flask App         |
| app.py            |
+-------------------+
     |
     +-------------------+
     |                   |
     v                   v
+-----------+     +-------------+
| Logging   |     | SQLite DB   |
| app.log   |     | students.db |
+-----------+     +-------------+
                        |
                        v
               +----------------+
               | students table |
               +----------------+
                        |
                        v
               +----------------+
               | Student Data   |
               +----------------+
```

---

# 🔄 Student Add Flow

```text
User
  |
  v
Add Student Form
  |
  v
/add
  |
  v
Flask Route
  |
  v
SQLite INSERT
  |
  v
students.db
  |
  v
Student Saved
```

---

# 📖 Student View Flow

```text
User
  |
  v
/students
  |
  v
Flask Route
  |
  v
SELECT * FROM students
  |
  v
SQLite Database
  |
  v
Student Records
  |
  v
students.html
  |
  v
Display Student List
```

---

# 🔍 Student Search Flow

```text
User
  |
  v
/search
  |
  v
Enter Student Name
  |
  v
Flask Route
  |
  v
SELECT * FROM students
WHERE name=?
  |
  v
SQLite Database
  |
  v
Search Results
  |
  v
Display Results
```

---

# ✏️ Student Update Flow

```text
User
  |
  v
/update
  |
  v
Flask Route
  |
  v
UPDATE students
SET marks=95
WHERE id=1
 

