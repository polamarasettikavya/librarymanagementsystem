
# 📚 Library Book Management System

A simple **console-based Python application** to manage a library's book inventory and student transactions. This beginner-friendly project helps you understand the basics of Python including file handling, dictionaries, user input, and date handling.

## ✅ Features

- 📖 Add or remove books  
- 👨‍🎓 Issue and return books to/from students  
- ⏳ Fine calculation for late returns (₹5 per day)  
- 💾 Data stored in JSON files for persistence  
- 📋 View available and issued books

## 🛠 Technologies Used

- Python 3
- JSON (for file storage)
- `datetime` module

## 📁 Project Structure

```
library_management_system/
│
├── books.json         # Stores book information
├── students.json      # Stores student issued book data
├── library.py         # Main Python script
└── README.md          # Project documentation
```

## ▶️ How to Run the Project

1. **Clone or Download the Code**  
   Save the `library.py` file to a folder on your system.

2. **Open Terminal or Command Prompt**  
   Navigate to the project folder:
   ```bash
   cd path_to_folder
   ```

3. **Run the Script**
   bash
   python library.py

4. **Follow the Menu**
   Use the number keys to choose an action (e.g., add book, issue book, return book, etc.)

## 💡 Example Flow


--- Library Management ---
1. Add Book
2. Remove Book
3. Issue Book
4. Return Book
5. View Books
6. View Issued Books
7. Exit
Enter your choice:


## 🧠 What You Will Learn

- File handling using JSON in Python
- Working with dates using the `datetime` module
- Writing and organizing Python functions
- Implementing basic CRUD operations
- Creating a simple terminal-based user interface

## 📌 Future Enhancements (Optional)

- Add unique student IDs
- Search functionality for books
- Support for multiple books per student
- GUI version using Tkinter

## 📬 Contact

For any questions or feedback, feel free to reach out via GitHub or email.
