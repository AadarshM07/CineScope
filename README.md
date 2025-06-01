# 🎬 CineScope: The Data Curator's Challenge

Welcome, Recruit! 🎉

You’ve just joined CineScope Studios, where movies are not only made but studied, filtered, and presented with precision. The UI team has already put together a sleek interface for visualizing our ever-growing movie archive — but they need **your skills** to connect it to the data and make it functional.

Are you ready to become CineScope’s data hero? Let’s go!

---

## 🛠️ What is CineScope?

CineScope is a mini-project that acts as a **movie database visualizer**, built using:

- **Python**
- **PySide6** (Qt-based GUI)
- **MySQL**
- **CSV data (movies.csv)**

The user interface is already provided. Your mission is to:

- Set up a SQL backend
- Populate it with movie data
- Write the backend logic to filter, display, and export movie data based on user input

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.x installed
- MySQL installed on your Linux system  
  👉 [Install MySQL on Linux (Official Guide)](https://dev.mysql.com/doc/mysql-apt-repo-quick-guide/en/#apt-repo-fresh-install)
- A code editor (VSCode recommended)
- Basic knowledge of:
  - SQL (SELECT, WHERE, LIKE, etc.)
  - Python
  - GUI fundamentals (optional)

---

## 🧳 What's Provided

- Fully built **PySide6 UI**
- `movies.csv` — a dataset of movies for your database
- Basic project structure

You **do not** need to create the UI — just connect the logic.

---

## 🎯 Your Mission

### 🗂️ Step 1: Prepare Your Database

1. Install and configure MySQL on your system.
2. Create a database (e.g., `cinescope`).
3. Create a table to hold movie data.
4. Import the provided `movies.csv` file into the MySQL table.

---

### 🧠 Step 2: Understand the UI Flow

- The UI has:
  - Filter buttons (e.g., by Genre, Year, Rating)
  - A text input box for arguments
  - Column selector buttons
  - A table to display results
  - An **Export to CSV** button

Your job is to:

- Capture button and input interactions
- Build an SQL query dynamically using the filter + argument
- Retrieve the result from MySQL
- Display it in the UI table

---



### 💾 Step 3: Add Export to CSV

- The visualized data should be exportable to a CSV file
- Create an **Export data** button
- On clicking the **Export data** button, write the current table data to a CSV like `output.csv`

---

## 🧹 Guidelines

- Keep your code readable and organized
- Use functions and avoid writing everything in one file
- Add comments where necessary
- Test your code with various filters and inputs

---


## 📚 Need Help?

- Learn basic SQL: https://www.w3schools.com/sql/
- PySide6 tutorials: https://doc.qt.io/qtforpython/
- Python + MySQL: https://pynative.com/python-mysql-database-connection/

---

## 📬 Submitting

- Push your completed code to a GitHub repository
- Include a `README.md` explaining your approach 

---

Good luck, and welcome to CineScope Studios — where data meets drama! 🍿
