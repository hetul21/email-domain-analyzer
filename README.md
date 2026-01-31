
# Email Domain Analyzer (Python & SQLite)

## Project Overview
The Email Domain Analyzer is a Python application that reads an email log file, extracts email domains, and stores domain frequency counts in an SQLite database. The project demonstrates backend logic, file handling, string parsing, and relational database operations.

This project was built as part of academic coursework to practice Python programming and database integration.

---

## Technologies Used
- Python 3
- SQLite
- SQL (SELECT, INSERT, UPDATE)
- File Handling
- String Processing

---

## How It Works
1. Reads an email log file (e.g., `mbox.txt`)
2. Identifies lines starting with `From `
3. Extracts email addresses from those lines
4. Parses the domain name (text after `@`)
5. Stores domain counts in an SQLite database
6. Displays domain frequency sorted in descending order

---

## Database Schema
**Table: Counts**

| Column | Type    | Description              |
|------|--------|--------------------------|
| org  | TEXT   | Email domain name        |
| count| INTEGER| Number of occurrences   |

---

## How to Run the Project
1. Make sure Python 3 is installed
2. Place an email log file (e.g., `mbox.txt`) in the same folder
3. Run the program:

```bash
python email_domain_analyzer.py
