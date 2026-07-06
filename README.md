# Student Management System

A lightweight, terminal-based Student Management System built using Python. This application allows users to perform CRUD (Create, Read, Update, Delete) operations on student records directly from the command line using Object-Oriented Programming (OOP) concepts.

## 🚀 Features

* **Add Student:** Create new student profiles with unique IDs, names, ages, and marks.
* **Duplicate Prevention:** Automatically checks if a Student ID already exists before adding a record.
* **View Records:** Display all stored student profiles in a clean format.
* **Search Profiles:** Quickly look up specific students using their unique ID.
* **Update Records:** Modify individual fields (ID, name, age, or marks) for any existing student.
* **Delete Student:** Permanently remove a student record from the system.

## 🛠️ Prerequisites

* **Python 3.x** installed on your system.

## 💻 How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   ```
2. **Navigate into the project directory:**
   ```bash
   cd student-management
   ```
3. **Execute the script:**
   ```bash
   python main.py
   ```

## 🏗️ Code Structure

* `Student` Class: Handles data blueprint and formatting for individual student objects.
* `while` Menu Loop: Drives the interactive command-line interface.
* In-Memory List: Stores student profiles dynamically during runtime.

## 📝 License

This project is open-source and free to use.
