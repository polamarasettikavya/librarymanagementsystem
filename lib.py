import datetime
import json
import os

# File paths
BOOKS_FILE = "books.json"
STUDENTS_FILE = "students.json"
FINE_PER_DAY = 5  # Rupees per day after due date


# Load or initialize data
def load_data():
    if os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, "r") as f:
            books = json.load(f)
    else:
        books = {}

    if os.path.exists(STUDENTS_FILE):
        with open(STUDENTS_FILE, "r") as f:
            students = json.load(f)
    else:
        students = {}

    return books, students


def save_data(books, students):
    with open(BOOKS_FILE, "w") as f:
        json.dump(books, f, indent=4)
    with open(STUDENTS_FILE, "w") as f:
        json.dump(students, f, indent=4)


# Add a new book
def add_book(books):
    book_id = input("Enter Book ID: ")
    if book_id in books:
        print("Book ID already exists.")
        return
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    books[book_id] = {"title": title, "author": author, "issued": False}
    print("Book added successfully.")


# Remove a book
def remove_book(books):
    book_id = input("Enter Book ID to remove: ")
    if book_id in books:
        if books[book_id]["issued"]:
            print("Book is currently issued and cannot be removed.")
        else:
            del books[book_id]
            print("Book removed.")
    else:
        print("Book not found.")


# Issue book
def issue_book(books, students):
    book_id = input("Enter Book ID to issue: ")
    student_name = input("Enter Student Name: ")

    if book_id not in books:
        print("Book not found.")
        return

    if books[book_id]["issued"]:
        print("Book already issued.")
        return

    issue_date = datetime.date.today()
    due_date = issue_date + datetime.timedelta(days=14)

    books[book_id]["issued"] = True
    students[student_name] = {
        "book_id": book_id,
        "issue_date": str(issue_date),
        "due_date": str(due_date)
    }
    print(f"Book issued to {student_name}. Due date: {due_date}")


# Return book and calculate fine
def return_book(books, students):
    student_name = input("Enter Student Name: ")

    if student_name not in students:
        print("No book issued by this student.")
        return

    data = students[student_name]
    book_id = data["book_id"]
    due_date = datetime.datetime.strptime(data["due_date"], "%Y-%m-%d").date()
    return_date = datetime.date.today()

    if return_date > due_date:
        days_late = (return_date - due_date).days
        fine = days_late * FINE_PER_DAY
        print(f"Book returned late. Fine: ₹{fine}")
    else:
        print("Book returned on time. No fine.")

    books[book_id]["issued"] = False
    del students[student_name]


# Display all books
def view_books(books):
    if not books:
        print("No books in library.")
        return
    for book_id, info in books.items():
        status = "Issued" if info["issued"] else "Available"
        print(f"{book_id} - {info['title']} by {info['author']} [{status}]")


# Display all students and issued books
def view_students(students):
    if not students:
        print("No books issued.")
        return
    for student, data in students.items():
        print(f"{student} - Book ID: {data['book_id']}, Due: {data['due_date']}")


# Main menu
def main():
    books, students = load_data()

    while True:
        print("\n--- Library Management ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. View Books")
        print("6. View Issued Books")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book(books)
        elif choice == "2":
            remove_book(books)
        elif choice == "3":
            issue_book(books, students)
        elif choice == "4":
            return_book(books, students)
        elif choice == "5":
            view_books(books)
        elif choice == "6":
            view_students(students)
        elif choice == "7":
            save_data(books, students)
            print("Data saved. Exiting...")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main() 